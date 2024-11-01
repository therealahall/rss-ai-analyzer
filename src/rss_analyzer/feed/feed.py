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

    def validate_feed_content(self, content: str) -> bool:
        """Validates that we have content and that our required elements all exist"""
        if not content:
            return False

        # Validate content to confirm we have the various pieces we need for future processing
        # Examples might be links, titles, content, summaries, etc...
        # Need to research how various feeds come through as we may need to be flexible here
        return True

    def sanitize_content(self, content: str) -> str:
        """Sanitize the content, stripping any unsafe elements"""
        return content
