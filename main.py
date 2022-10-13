import ssl
import json
import socket as S
import logging
import unittest
from pprint import pprint

CONSUMER_KEY = "SMkvCrIgyfPDvGnJSLrI"
CONSUMER_SECRET = "NsEZUIIcKegWRHInGhLGuVfBYXfwjKp"

class DiscogAPIInterface():
    def __init__(self, isPresentation = False):
        # isPresentation espera input apos certas acoes
        self.set_logging()
        logging.info("Pedimos ao OS um socket que implementa a familia de protocolos")
        logging.info("  IPv4 (family=AF_INET) e de tipo SOCK_STREAM, ou seja: 'reliable, ")
        logging.info("  stream-oriented e full duplex'. Este é o tipo de socket sobre o qual")
        logging.info("  o protocolo TCP é implementado.")
        logging.info("  Referências: `man 2 socket` e `man 7 tcp`")
        self.sock = S.socket(family=S.AF_INET, type=S.SOCK_STREAM)

        logging.info("Usamos a função SSLContext.wrap_socket(self.sock) para criar um wrapper sobre")
        logging.info("  sobre o nosso socket implementando o protocolo TLS/SSL. Isto é feito ")
        logging.info("  pois a API que será consumida é em HTTPS, isto é, HTTP sobre TLS. Note-se")
        logging.info("  que os protocolos HTTP e TLS são da camada de aplicação (camada 7).")
        logging.info("Estabelecemos conexão com o servidor usando SSLSocket.connect_ex")
        logging.info("  para abstrair sobre o protocolo TLS. Assim não precisamos implementar")
        logging.info("  relacionado ao protocolo")
        ssl_context = ssl.create_default_context()
        self.ssl_sock = ssl_context.wrap_socket(self.sock, server_hostname='api.discogs.com')

        errno = self.ssl_sock.connect_ex(('api.discogs.com', 443))
        if errno != 0:
            logging.error(f"connect_ex erro {errno}. Saindo")
            exit(1)
        logging.info("Estabelecemos com sucesso uma conexão com o servidor usando a ")
        logging.info("  interface oferecida por SSLSocket.")

    def set_logging(self):
        logging.basicConfig(format='(%(asctime)s)%(levelname)s: %(message)s.', datefmt='%H:%M:%S', level=logging.DEBUG)

    def queryArtistInfo(self, artist_id):
        return {}

def main():
    dapi = DiscogAPIInterface()
    print(dapi.queryArtistInfo('465904'))
    pass

if __name__ == "__main__":
    main()


#import socket
#
#HOST = 'example.com'    # The remote host
#PORT = 80              # The same port as used by the server
#http_msg = (b"GET / HTTP/1.1\n"
#            b"Host: example.com\n"
#            b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0\n"
#            b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\n"
#            b"Accept-Language: en-US,en;q=0.5\n"
#            b"Accept-Encoding: gzip, deflate\n"
#            b"Connection: keep-alive\n"
#            b"Upgrade-Insecure-Requests: 1\n"
#            b"If-Modified-Since: Thu, 17 Oct 2019 07:18:26 GMT\n")
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(http_msg)
#    data = s.recv(2048)
#print('Received', repr(data))
#
#
###def main():
##    HOST = 'tcpbin.com'    # The remote host
##    PORT = 4242              # The same port as used by the server
##    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
##        s.connect((HOST, PORT))
##        s.sendall(b'Hello, world')
##        data = s.recv(1024)
##    print('Received', repr(data))
##    pass
##
##if __name__ == "__main__":
##    main()
#
#
