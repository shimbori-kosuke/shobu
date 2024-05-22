import socket

class Client:  # クライアント側(送信側の処理)

    def __init__(self,q):
        self.q = q

    def c2s(self, ip, port, x,y):  # サーバー側へ送信
        s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serv_address = (ip, port)
        msg = f"{x},{y}"
        s.sendto(msg.encode('utf-8'), serv_address)
