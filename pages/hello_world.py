from status_code import StatusCode


class HelloWorld:
    @staticmethod
    def get_code_and_content(uri):
        return StatusCode.OK, "<html><body>Hello, world!</body></html>"
