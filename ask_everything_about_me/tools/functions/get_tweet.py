import re
from typing import List

import tweepy

from ask_everything_about_me.config import settings


def clean_text(tweet: str) -> str:
    """
    remove link and reply

    Args:
        tweet (str): raw_tweet

    Returns:
        str: tweet after removing link and reply
    """
    result = re.sub("https?://[\w!\?/\+\-_~=;\.,\*&@#\$%\(\)'\[\]]+", "", tweet)
    result = re.sub("@[\\w]{1,15}", "", result)
    return result


def get_recent_tweet(top_k: int = 10) -> List[str]:
    if all(
        settings.tweet_api_key
        and settings.tweet_api_key_secret
        and settings.tweet_access_token
        and settings.tweet_access_token_secret
    ):

        auth = tweepy.OAuthHandler(
            settings.tweet_api_key,
            settings.tweet_api_key_secret,
        )
        auth.set_access_token(
            settings.tweet_access_token,
            settings.tweet_access_token_secret,
        )
        api = tweepy.API(auth)
        return [
            clean_text(tweet.text)
            for tweet in tweepy.Cursor(
                api.user_timeline, id=settings.twitter_account
            ).items(top_k)
        ]
    else:
        return "We could not get tweet since no certification"


def get_recent_tweet_for_tool(top_k: str = "10"):
    top_k = int(top_k)
    return "/".join(get_recent_tweet(top_k))
