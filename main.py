import socket

HOST = 'example.com'    # The remote host
PORT = 80              # The same port as used by the server
http_msg = (b"GET / HTTP/1.1\n"
            b"Host: example.com\n"
            b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0\n"
            b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n"
            b"Accept-Language: en-US,en;q=0.5\n"
            b"Accept-Encoding: gzip, deflate\n"
            b"Connection: keep-alive\n"
            b"Upgrade-Insecure-Requests: 1\n"
            b"If-Modified-Since: Thu, 17 Oct 2019 07:18:26 GMT\n")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(http_msg)
    data = s.recv(2048)
print('Received', repr(data))


##def main():
#    HOST = 'tcpbin.com'    # The remote host
#    PORT = 4242              # The same port as used by the server
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.connect((HOST, PORT))
#        s.sendall(b'Hello, world')
#        data = s.recv(1024)
#    print('Received', repr(data))
#    pass
#
#if __name__ == "__main__":
#    main()


