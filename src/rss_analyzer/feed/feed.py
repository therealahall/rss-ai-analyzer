import validators
from rss_analyzer.exceptions import InvalidUrlException


class Feed:
    url: str

    def __init__(self, url: str) -> None:
        if not validators.url(url):
            raise InvalidUrlException(f"Invalid URL {url}")

        self.url = url

    def __repr__(self) -> str:
        return f"{type(self).__name__}(url='{self.url}')"
