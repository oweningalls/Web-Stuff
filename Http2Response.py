class Http2Response:
    content = ""
    status_code = 0

    def build_response(self):
        return f"""\
HTTP/2 {self.status_code} 

{self.content}\
"""

    def set_content(self, content):
        self.content = content
        return self

    def set_status_code(self, code):
        self.status_code = code
        return self

