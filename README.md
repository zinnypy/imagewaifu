
# 🎀 ImageWaifu 🎀

✨ Transform your profile picture into an adorable chibi version! ✨

This is a Twitter bot that automatically generates chibi-style versions of users' profile pictures when they interact with the bot. Powered by AI image generation, it delivers cute and personalized avatars with a single mention!
# 🚀 How It Works

Tag the bot in a post with the following text:

"@imagewaifu chibi me"  

The bot will reply with your chibi-styled avatar!
## 🔧 Features

- Scans the bots mentions
- Completely automated, no need to even log in to the account.
- Custom stable diffusion model to generate Chibi version of users profile picture


## ⚙️ Tech Stack

**Bot:** 100% Python

**AI Image Generation:** 100% Python


## 📡 Deployment

To deploy the bot first you have to create the following environment variables:

```
TWITTER_API_KEY=<Your X/Twitter API Key>
TWITTER_API_SECRET_KEY=<Your X/Twitter API Secret Key>
TWITTER_ACCESS_TOKEN=<Your X/Twitter Access Token>
TWITTER_ACCESS_SECRET=<Your X/Twitter Access Secret>
```

Then you simply run the following:

```bash
pip install -r requirements.txt
python bot.py
```


## 🔎 Authors

- [@zinnypy](https://www.github.com/zinnypy)

