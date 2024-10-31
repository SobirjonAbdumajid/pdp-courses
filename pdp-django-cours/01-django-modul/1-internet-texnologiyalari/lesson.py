import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    s.connect(("42.uz", 80)) # shu kod bajarilsa serverga ulandi ya'ni aloqa bor degani
    s.send(b"""GET / HTTP/1.1\r\nHOST: 42.uz\r\n\r\n""")
    print(s.recv(1024))