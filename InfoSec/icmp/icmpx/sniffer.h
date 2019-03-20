#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <pcap.h>

#include <sys/socket.h>
#include <net/ethernet.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>

#define SNAP_LEN 65535
#define PORMISC 1
#define TO_MS 0
#define COMPILE_OPTIMIZE 0
#define LOOP_TO_FAULT -1
#define SIZE_ETHERNET 14

#define ETHERTYPE_IP 0x0800 /* IP protocol */

bpf_u_int32 mask;		/* Our netmask */
bpf_u_int32 net;		/* Our IP */
uint32_t target_src;

int capture_packet();