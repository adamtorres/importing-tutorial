import contextlib
from http import HTTPStatus, server
import io
import socket


class DualStackServer(server.ThreadingHTTPServer):
    def server_bind(self):
        # suppress exception when protocol is IPv4
        with contextlib.suppress(Exception):
            self.socket.setsockopt(
                socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        return super().server_bind()


class BogusHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        path = self.translate_path(self.path)
        if path.endswith("/circular_b.py"):
            content = "This is the custom content for the one file. "
            content += "All others will be normal."
            encoded = content.encode("utf-8", "surrogateescape")
            f = io.BytesIO()
            f.write(encoded)
            f.seek(0)
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-Length", str(len(encoded)))
            self.send_header("Last-Modified", self.date_time_string())
            self.end_headers()
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
        else:
            super().do_GET()


if __name__ == '__main__':
    server.test(
        HandlerClass=BogusHTTPRequestHandler,
        ServerClass=DualStackServer,
        port=8000,
        bind="0.0.0.0",
    )
