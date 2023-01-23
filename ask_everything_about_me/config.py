import os
from typing import Optional

from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    ## Basic
    openai_api_key: str = ""
    interviewee_name: str = ""

    ## for get url
    twitter_account: Optional[str] = None
    twitter_url: Optional[HttpUrl] = (
        f"https://twitter.com/{twitter_account}" if twitter_account else None
    )
    facebook_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None

    ## for get tweets
    tweet_api_key: Optional[str] = None
    tweet_api_key_secret: Optional[str] = None
    tweet_access_token: Optional[str] = None
    tweet_access_token_secret: Optional[str] = None
    tweet_bearer_token: Optional[str] = None

    ## for get tweets
    max_tokens: int = 512
    base_embeddings: str = "openai"
    chunk_size: int = 500
    chunk_overlap: int = 20
    HyDE_n: int = 4
    HyDE_best_of: int = 4

    similarity_search_k: int = 3
    reset_docsearch: bool = False
    docsearch_path: Optional[str] = "ask_everything_about_me/data/docsearch.pickle"

    ## for direct contact
    gmail_account: Optional[str] = None
    gmail_password: Optional[str] = None


settings = Settings()
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
