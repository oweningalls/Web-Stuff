import string


class Http1_1Request:
    method = ""
    uri = ""
    headers = {}
    body = None

    def __init__(self, request_text: string):
        request_text = request_text.splitlines()
        request_line = request_text[0].split(" ")
        self.method = request_line[0]
        self.uri = request_line[1][1:]
        if request_line[2] != "HTTP/1.1":
            raise ValueError(f"HTTP version was not 1.1: '{request_line[2]}'")

        i = 3
        has_body = False
        while i < len(request_text):
            line = request_text[i]
            if line == "":
                has_body = True
                break

            parts = line.split(": ", 1)
            self.headers[parts[0]] = parts[1]
            i += 1

        if not has_body:
            return

        i += 1
        self.body = "\n".join(request_text[i:])

    def list_parts(self):
        return f"""\
method: {self.method}
uri: {self.uri}
body: {self.body}
headers: {self.headers}\
"""
