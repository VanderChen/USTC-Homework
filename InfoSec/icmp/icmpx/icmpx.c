#include "icmpx.h"

int main(int argc, char **argv)
{   
    int opt = 0;
    char* dev;
    char target_ip[INET_ADDRSTRLEN] = "";
    char gateway[INET_ADDRSTRLEN];
    while((opt = getopt(argc,argv,"d:g:")) != -1){
        switch (opt)
        {
            case 'd':
                strcpy(target_ip,optarg);
                break;
            case 'g':
                strcpy(gateway,optarg);
                break;
            default:
                break;
        }
    }
    capture_packet(target_ip,gateway);
    
    return 0;
}
