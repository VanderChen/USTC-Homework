# coding = utf-8

import os
import socket
import time
import select
import struct


ICMP_ECHO_REQUEST = 8

# 检验和算法
def checksum(source_string):
    sum = 0
    count = 0 #起到计数作用
    max_count = (len(source_string)/2)*2
    while count < max_count:
        # 将数据分隔为每两比特一组共16位，并将其相加(前面一个bite高后面一个bite8位二进制所以乘上256)
        thisVal = source_string[count + 1]*256 + source_string[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff #进行与运算  表示只保留sum的低32数据防止溢出
        count = count + 2
    if max_count < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff
    #将高16bit与低16bit反复相加，直到高16bit的值为0，从而获得一个只有16bit长度的值
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer # 返回十进制整数

# 接收ping命令所花费的时间
def receive_ping(sock, id, timeout):
    time_left = timeout
    while True:
        starttime = time.time()
        """
        select()函数 在time_left时间内阻塞程序的执行,监视sock套接字，当套接字满足可读条件时将套接字返回给readable，然后程序继续执行
        """
        readable  = select.select([sock], [], [], time_left)
        wait_time = (time.time() - starttime) # 等待的时间
        if readable[0] == []:                 # 在timeout时间内未满足条件
            return

        time_received = time.time()
        #接收发送的UDP数据 返回值为(data,address)其中data是包含接收数据的字符串，address是发送数据套接字地址
        rcv_data, addr = sock.recvfrom(1024)
        icmp_header = rcv_data[20:28] #icmp头部信息
        type, code, checksum, packetID, sequence = struct.unpack(
            "bbHHh", icmp_header
        )
        # type = 8 表示ping请求  在ICMP报文中有规定
        if type != 8 and packetID == id:
            bytesInDouble = struct.calcsize("d")
            time_sent = struct.unpack("d", rcv_data[28:28 + bytesInDouble])[0] #解包 获取time_sent时间
            return time_received - time_sent

        time_left = time_left - wait_time
        if time_left <= 0:
            return

def send_ping(sock, dest_addr, id):
    dest_addr = socket.gethostbyname(dest_addr)# 将域名解析为IPv4地址
    checksum1 = 0 # 检验和
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, checksum1, id, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "Q"
    data = struct.pack("d", time.time()) + data.encode()# 将数据转换为字节流

    checksum1 = checksum(header + data) # 对发送ICMP计算检验和
    """
    socket.ntohs=net  to host short int 16位
    socket.htons=host to net  short int 16位
    socket.ntohl =net to host long  int 32位
    socket.htonl=host to net  long  int 32位
    """
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(checksum1), id, 1
    )
    packet = header + data
    sock.sendto(packet, (dest_addr, 1))

def do(dest_addr, timeout):
    icmp = socket.getprotobyname("icmp")# 来指定协议的类型
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)# 来创建套接字
    my_ID = os.getpid() & 0xFFFF #得到进程号
    send_ping(sock, dest_addr, my_ID)
    delay = receive_ping(sock, my_ID, timeout)
    sock.close()
    return delay

def ping(dest_addr, timeout = 2, count = 4):
    print(u"ping {}...".format(dest_addr))
    for i in range(count):
        delay  =  do(dest_addr, timeout)
        if delay  ==  None:
            print(u"failed. (timeout within {}sec.)".format(timeout))
        else:
            delay  =  delay * 1000
            print(u"get ping in {}ms".format(int(delay)))

if __name__ == '__main__':
    while True:
        try:
            cmd = input('Please input the ip address you want to ping(Input exit to end the ping) :')
            if cmd == '' or cmd == 'exit':
                break
            ping(cmd)
        except EOFError:
            break