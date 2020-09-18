import contextlib
from http import server
import socket


class DualStackServer(server.ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()


if __name__ == '__main__':
    server.test(
        HandlerClass=server.SimpleHTTPRequestHandler,
        ServerClass=DualStackServer,
        port=8000,
        bind="0.0.0.0",
    )
