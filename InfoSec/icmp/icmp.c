#include "icmp.h"

int main(int argc, char **argv)
{   
    int opt = 0;
    while((opt = getopt(argc,argv,"s:d")) != -1){
        switch (opt)
        {
            case 's':
                printf("this is s");
                printf(optarg);
                break;
            case 'd':
                printf("this is d");
                break;
            default:
                printf("this is nothing");
                break;
        }
    }
    
    return 0;
}
