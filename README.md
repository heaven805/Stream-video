# Telegram Video Player Bot (Beta)
![GitHub Repo stars](https://img.shields.io/github/stars/mohsinhsn/Stream-video?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/mohsinhsn/Stream-video?color=green&style=flat)

A Telegram Bot By [@StylishUser](https://t.me/StylishUser) To Stream Videos in Telegram Voice Chat.

## Main Features
- Supports Live Streaming
- Supports YouTube Streaming
- Supports Live Radio Streaming
- Supports Video Files Streaming
- Supports YouTube Live Streaming
- Customizable Userbot Protection (PM Guard)

## Deploy Own Bot

### Railway (Reommanded)
<p><a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FMohsinHsn%2FStream-video&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CSESSION_STRING%2CCHAT_ID%2CAUTH_USERS%2CBOT_USERNAME%2CREPLY_MESSAGE&optionalEnvs=REPLY_MESSAGE&API_IDDesc=User+Account+Telegram+API_ID+get+it+from+my.telegram.org%2Fapps&API_HASHDesc=User+Account+Telegram+API_HASH+get+it+from+my.telegram.org%2Fapps&BOT_TOKENDesc=Your+Telegram+Bot+Token%2C+get+it+from+%40Botfather+XD&SESSION_STRINGDesc=Pyrogram+Session+String+of+User+Account%2C+get+it+from+%40genStr_robot&CHAT_IDDesc=ID+of+your+Channel+or+Group+where+the+bot+will+works+or+stream+videos&AUTH_USERSDesc=ID+of+Auth+Users+who+can+use+Admin+commands+%28for+multiple+users+seperated+by+space%29&BOT_USERNAMEDesc=Your+Telegram+Bot+Username+without+%40%2C+get+it+from+%40Botfather+XD&REPLY_MESSAGEDesc=A+reply+message+to+those+who+message+the+USER+account+in+PM.+Make+it+blank+if+you+do+not+need+this+feature.&REPLY_MESSAGEDefault=Hello+Sir%2C+I%27m+a+bot+to+stream+videos+on+telegram+voice+chat%2C+not+having+time+to+chat+with+you+%F0%9F%98%82%21&referralCode=SAFONE"><img src="https://img.shields.io/badge/Deploy%20To%20Railway-blueviolet?style=for-the-badge&logo=railway" width="200""/></a></p>

### Heroku (Don't Complain)
<p><a href="https://heroku.com/deploy?template=https://github.com/MohsinHsn/Stream-video"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

## Commands (Botfather)
```sh
start - Start The Bot
help - Show Help Message
radio - Start Radio Streaming
stream - Start Video Streaming
endstream - Stop Streaming & Left VC
```

## Config Vars
1. `API_ID` : User Account Telegram API_ID, get it from my.telegram.org
2. `API_HASH` : User Account Telegram API_HASH, get it from my.telegram.org
3. `BOT_TOKEN` : Your Telegram Bot Token, get it from @Botfather XD
4. `BOT_USERNAME` : Your Telegram Bot Username, get it from @Botfather XD
4. `SESSION_STRING` : Pyrogram Session String of User Account, get it from [@genStr robot](http://t.me/genStr_robot) or [![genStr](https://img.shields.io/badge/repl.it-genStr-yellowgreen)](https://repl.it/@AsmSafone/genStr)
5. `CHAT_ID` : ID of Channel/Group where the bot will works or stream videos.
6. `AUTH_USERS` : ID of Users who can use Admins commands (for multiple users seperated by space).
7. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature.

## Requirements
- Python 3.6 or Higher.
- Latest [FFmpeg Python](https://www.ffmpeg.org/).
- [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api).
- Pyrogram [String Session](http://t.me/genStr_robot) Of The Account.
- The User Account Needs To Be An Admin In The Group / Channel.

## Self Host
```sh
$ git clone https://github.com/MohsinHsn/Stream_video.git
$ cd Stream-video
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
# <create .env variables appropriately>
$ python3 -m bot
```


## License
Streaming bot, Telegram Video Chat Bot


## Credits

- [Monstar](https://github.com/MohsinHsn) for [Editing 😜](https://github.com/MohsinHsn/Stream-video) ☠️
- [Safone](https://github.com/AsmSafone) for [Noting](https://github.com/AsmSafone/VideoPlayerBot) 😬
- [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram) ❤️
- [MarshalX](https://github.com/MarshalX) for [pytgcalls](https://github.com/MarshalX/tgcalls) ❤️
