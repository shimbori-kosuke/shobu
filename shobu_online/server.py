import socket
import threading

import config as con

class Server():#サーバー側(受信側の処理)
    def __init__(self,q):
        self.q = q
        self.host = con.SERVER_HOST
        self.port = con.SERVER_PORT
        self.bufsize = con.SERVER_BUFSIZE

        self.sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        self.thread = threading.Thread(target=self.c2s, daemon=True)
        self.thread.start()

    def c2s(self):#サーバー側へ受信
        try:
            while True:
                msg, cli_addr = self.sock.recvfrom(self.bufsize)
                pos = tuple(msg.decode('utf-8').split(','))
                self.q.put(pos)
                print(msg)
                print(pos)
        except Exception as e:
            print(e)

        # self.sock.close()  