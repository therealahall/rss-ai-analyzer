import pytest
from rss_analyzer.feed import Feed
from rss_analyzer.exceptions import InvalidUrlException


def test_valid_url() -> None:
    valid_url = "https://www.example.org"
    invalid_url = "invalid url"

    with pytest.raises(InvalidUrlException):
        Feed(invalid_url)

    rss_feed = Feed(valid_url)
    assert rss_feed.url == valid_url
