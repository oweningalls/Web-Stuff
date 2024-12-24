import socket

from HelloWorld import HelloWorld
from Http1_1Request import Http1_1Request
from Http2Response import Http2Response
from Router import Router
from ServeStatusCode import ServeStatusCode
from StatusCode import StatusCode

HOST = "localhost"
PORT = 8080


def main():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    router = Router()
    router.add_route("status_code/.*", ServeStatusCode.get_code_and_content)
    router.add_route("hello_world", HelloWorld.get_code_and_content)

    conn = None
    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")

            request_text = conn.recv(1024).decode("utf-8")
            print(request_text)
            request = Http1_1Request(request_text)

            status_code, content = router.get_code_and_content(request.uri)

            (Http2Response()
             .set_content(content)
             .set_status_code(status_code)
             .send_response(conn))

        except Exception as e:
            print(e)
            if conn is None:
                continue
            status_code = StatusCode.INTERNAL_SERVER_ERROR
            (Http2Response()
             .set_content(status_code.name)
             .set_status_code(status_code.value)
             .send_response(conn))
            conn.close()
    server_socket.close()


if __name__ == '__main__':
    main()
