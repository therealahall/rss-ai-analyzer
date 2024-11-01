"""Import the URL validation to ensure we have a valid URl before processing anything"""

from validators import url as validateUrl
from rss_analyzer.exceptions import InvalidUrlException


class Feed:
    """Our custom feed class to manage content coming from RSS feeds"""

    url: str

    def __init__(self, url: str) -> None:
        if not validateUrl(url):
            raise InvalidUrlException(f"Invalid URL {url}")

        self.url = url

    def __repr__(self) -> str:
        return f"{type(self).__name__}(url='{self.url}')"
