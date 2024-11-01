import argparse
from rss_analyzer.feed import Feed

parser = argparse.ArgumentParser("rss_analyzer")
parser.add_argument(
    "feed", help="Enter in an RSS feed URL such as https://example.org/rss.xml"
)
arguments = parser.parse_args()

feed = Feed(arguments.feed)
print(feed)
