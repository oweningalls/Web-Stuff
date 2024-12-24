import re

from status_code import StatusCode


class Router:
    patterns = []

    def add_route(self, pattern, get_code_and_content):
        self.patterns.append((pattern, get_code_and_content))

    def get_code_and_content(self, uri):
        for pattern, get_code_and_content in self.patterns:
            if self.route_matches(uri, pattern):
                return get_code_and_content(uri)

        return StatusCode.NOT_FOUND.value, StatusCode.NOT_FOUND.name

    @staticmethod
    def route_matches(uri, pattern):
        return re.search(f"^{pattern}$", uri) is not None

