import tweepy, os, re
from image import generate_image

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

def authenticate():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def check_mentions(api):
    mentions = api.mentions_timeline(count=20, tweet_mode='extended')
    for mention in mentions:
        mention_pattern = re.compile(r'^@imagewaifu chibi me', re.IGNORECASE)
        tweet_text = mention.full_text
        match = mention_pattern.match(tweet_text)
        if match:
            generate_from_tweet(mention, api)

def generate_from_tweet(tweet, api):
    user_handle = tweet.user.screen_name
    user_pfp_url = tweet.user.profile_image_url.replace("_normal", "")

    try:
        generated_image_url = generate_image(user_pfp_url)
        reply_to_user(tweet, generated_image_url, api)
    except Exception as e:
        reply_error(tweet, api)
        print(f'[ERR] Could not generate for @{user_handle}: {e}')

def reply_to_user(tweet, image_url, api):
    reply_text = f"@{tweet.user.screen_name} I made a Kawaii version of you! {image_url}"
    api.update_status(status=reply_text, in_reply_to_status_id=tweet.id)

def reply_error(tweet, api):
    reply_text = f"@{tweet.user.screen_name} Uh oh! Something went wrong... Please try me again soon!"
    api.update_status(status=reply_text, in_reply_to_status_id=tweet.id)
