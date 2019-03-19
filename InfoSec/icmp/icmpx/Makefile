icmpx : icmpx.c icmpx.h sniffer.o
	cc icmpx.c icmpx.h sniffer.o -o icmpx -lpcap

sniffer.o : sniffer.c sniffer.h

.PHONY : clean install

clean :
	rm *.o icmpx

install :
	cp icmpx /usr/local/bin/icmpx


# gcc icmp.h icmp.c sniffer.h sniffer.c -o icmp -lpcap