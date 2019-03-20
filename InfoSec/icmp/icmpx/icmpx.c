#include "icmpx.h"

int main(int argc, char **argv)
{   
    int opt = 0;
    char* dev;
    while((opt = getopt(argc,argv,"rd")) != -1){
        switch (opt)
        {
            case 'r':
                capture_packet();
                break;
            // case 'd':
            //     printf("this is d");
            //     break;
            default:
                printf("this is nothing");
                break;
        }
    }
    
    return 0;
}
