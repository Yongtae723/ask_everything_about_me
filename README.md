# 😆 Ask Everything About Me
![concept_art](/documents/concept_art.png)

This bot can do the following on your behalf
- Show you the URLs that are relevant to you.
- Analyze your tweets and show you what you are interested in these days.
- Answer questions about you from your blog or profile.

# 👀 Let's try!
You can try this bot from [here](https://about-yongtae-cfa5uiil5a-an.a.run.app/).

# ⭐ Use Case

The use cases I assume are as follows

- Individuals/companies can introduce themselves to individuals/companies
- When you don't know how to write your introduction, Bot can help you

I hope you will be able to customize this bot for your own use and use it to introduce yourself, especially as a job-seeking appeal.

# 🧠 Basic architecture
![architecture](/documents/architecture.png)

ZeroShotAgent uses the following tools for answering questions.
- **Get urls**: Returns pre-defined social media url.
- **Get recent tweets**: Returns the content of recent tweets. From this content, bot can reply to the recent interests and trends of the interviewee.
- **Question answering from docs**: Answer questions about you from pre-defined profiles, blogs, etc. The algorithm uses [HyDE](https://langchain.readthedocs.io/en/latest/modules/utils/combine_docs_examples/hyde.html?highlight=Hyde).


# 🚀 Quick Custom

## Basic
1. Set `openai_api_key`, `interviewee_name` in [config file](ask_everything_about_me/config.py) or environment variable

## Get urls
1. Set urls in [config file](ask_everything_about_me/config.py) or environment variable as much as you want.
2. Edit [service_name2url](ask_everything_about_me/tools/functions/get_url.py)


## Get recent tweets
1. get `tweet_api_key`, `tweet_api_key_secret`, `tweet_access_token` and `tweet_access_token_secret` from [twitter developer portal](https://developer.twitter.com/en/portal/projects-and-apps) and set those in [config file](ask_everything_about_me/config.py) or environment variable. If one of these are not set, this tool doesn't work.
2. confirm you `twitter_account` is set in [config file](ask_everything_about_me/config.py) or environment variable


## Question answering from docs
1. Add your profiles and blogs in [ask_everything_about_me/data](ask_everything_about_me/data)

## [Option] Contact directly.
Streamlit web app offer column for user to contact directly. If you want to use it, set `gmail_account` and `gmail_password` in [config file](ask_everything_about_me/config.py) or environment variable.

## Start App!

```
make startup_app
```

# 😍 Welcome contributions
if you find some error or feel something, feel free to tell me by PR or Issues!! Opinions on any content are welcome!

## What I want to do
- [ ] streamlit-chat icons with your free image