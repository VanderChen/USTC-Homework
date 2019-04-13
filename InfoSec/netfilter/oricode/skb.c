#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>

static struct nf_hook_ops nfho;
struct sk_buff * skbuff;
struct iphdr * iph;
struct tcphdr * tcph;

unsigned int hook_func(unsigned int hooknum,struct sk_buff *skb,const struct net_device *in,const struct net_device *out,int(okfn)(struct sk_buff *)){
	skbuff = skb;
	iph = ip_hdr(skbuff);
	printk("Network header is %u.\n",iph);	
	tcph = tcp_hdr(skbuff);	
	printk("Transport header is %u.\n",tcph);	
	printk("Transport header is %u.\n",skbuff->transport_header);	
	printk("Network header is %u.\n",skbuff->network_header);	
	printk("MAC header is %u.\n",skbuff->mac_header);	
	return NF_ACCEPT; 
}

int init_module(){
	nfho.hook = hook_func;
	nfho.hooknum = NF_INET_PRE_ROUTING;
	nfho.pf = PF_INET;
	nfho.priority = NF_IP_PRI_FIRST; 

	nf_register_hook(&nfho);
	return 0;

}

void cleanup_module(void){
	nf_unregister_hook(&nfho);
}
