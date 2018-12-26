import socket
import struct
import time

BUFSIZ = 4096

def main():

    address = ('0.0.0.0', 8000)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()  
    s.bind(address)  
    s.listen(1)
    ss, addr = s.accept()  
    print('成功连接',addr)
    ss.send("已连接！".encode())

    while True:

        rec = ss.recv(BUFSIZ)

        if rec == "exit":
            break

        print("收到：",rec.decode("utf-8"))
        send = input("发送： ")
        ss.send(send.encode())

        if rec == "exit":
            break

    ss.close()  
    s.close()  

if __name__ == '__main__':
    main()
