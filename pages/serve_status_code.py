from status_code import StatusCode


class ServeStatusCode:
    @staticmethod
    def get_code_and_content(uri):
        try:
            code = StatusCode(int(uri.split("/")[-1]))
        except:
            code = StatusCode.NOT_FOUND

        return code, code.name
