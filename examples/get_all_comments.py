"""
    Current, the length of comment continuation token increases over time to the point
    where the request is aborted with `414 Request-URI Too Large` error.

    This might be a bug in the API, or a Google bug. Either way or not, mass scraping of comments seems
    impossible right now. If you know a workaround, please open an issue/PR.
"""

try:
    from requests_cache import CachedSession as Session # type: ignore
except ImportError:
    from requests import Session

from requests import HTTPError
from invidious_api_client import InvidiousClient


def get_all_comments():
    CLIENT = InvidiousClient(additional_parameters={'hl': 'de'}, session_object=Session())

    try:
        for comments in CLIENT.yield_all_comments('9bZkp7q19f0'):
            for comment in comments:
                print(f"{comment.author} ({comment.published_text}): {comment.content}")
    
    except HTTPError as e:
        print(e)



if __name__ == "__main__":
    get_all_comments()
