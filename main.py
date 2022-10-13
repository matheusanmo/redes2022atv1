import ssl
import json
import socket as S
import logging
import unittest
from pprint import pprint

def dbg_die(msg):
    print(">>> DBG_DIE MSG BEGIN")
    pprint(msg)
    print(">>> DBG_DIE MSG END")
    input(">>> HIT ENTER TO EXIT")
    exit(1)

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
        response = bytearray()
        msg = bytearray()
        msg += b'GET /artists/465904 HTTP/1.1\r\n'
        msg += b'Host: api.discogs.com\r\n'
        msg += b'User-Agent: matheusanmoredes/0.1 +https://github.com/matheusanmo/redes2022atv1\r\n'
        msg += b'Authorization: Discogs token=rqaaEKqAJVpnZsPJfyYXuWOGZZZwTMWrAaMiRKJY\r\n'
        msg += b'\r\n'
        sent_bytes = self.ssl_sock.sendall(msg)
        while recv := self.ssl_sock.recv(4096):
            response += recv
            if recv == b'0\r\n\r\n':
                break
        dbg_die(response)
        #from IPython.core.debugger import set_trace; set_trace()

def main():
    dapi = DiscogAPIInterface()
    print(dapi.queryArtistInfo('465904'))
    pass

if __name__ == "__main__":
    main()

