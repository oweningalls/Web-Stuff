from enum import Enum


class StatusCode(Enum):
    OK = 200
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
