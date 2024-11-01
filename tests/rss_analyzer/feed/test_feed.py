import pytest
from rss_analyzer.feed import Feed
from rss_analyzer.exceptions import InvalidUrlException


def test_valid_url() -> None:
    valid_url = "https://www.example.org"
    rss_feed = Feed(valid_url)
    assert rss_feed.url == valid_url


def test_invalid_url() -> None:
    invalid_urls = [
        "invalid url",
        "http://",
        "definitely-not-a-url",
        "",
    ]

    for invalid_url in invalid_urls:
        with pytest.raises(InvalidUrlException):
            Feed(invalid_url)
