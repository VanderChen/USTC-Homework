#include "icmpx.h"

int main(int argc, char **argv)
{   
    int opt = 0;
    char* dev;
    while((opt = getopt(argc,argv,"d:")) != -1){
        switch (opt)
        {
            case 'd':
                capture_packet(optarg);
                return 0;
                break;
            default:
                break;
        }
    }
    capture_packet("");
    
    return 0;
}
