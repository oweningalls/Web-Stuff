import socket

from Http11Request import Http11Request
from Http2Response import Http2Response

HOST = "localhost"
PORT = 8080


def main():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")

            request_text = conn.recv(1024).decode("utf-8")
            print(request_text)
            request = Http11Request(request_text)

            response = (Http2Response()
                        .set_content(request.list_parts())
                        .set_status_code(200)
                        .build_response())
            conn.sendall(response.encode("utf-8"))

            conn.close()
    except Exception as e:
        print(e)
    finally:
        server_socket.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

