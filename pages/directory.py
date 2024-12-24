from status_code import StatusCode


class Directory:
    items = []

    def add_item(self, text, uri):
        self.items.append((text, uri))

    def get_code_and_content(self):
        content = "<h1>Directory</h1>"
        for text, uri in self.items:
            content += f"<div><a href=\"{uri}\">{text}</a></div>\n"

        return StatusCode.OK, content
