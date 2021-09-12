
import os
import re
from dotenv import load_dotenv

load_dotenv()

class db:
    VIDEO_CALL = {}
    RADIO_CALL = {}
    FFMPEG_PROCESSES = {}

class Config:
    ADMIN = os.environ.get("AUTH_USERS", "")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)
    API_ID = int(os.environ.get("API_ID", ""))
    CHAT_ID = int(os.environ.get("CHAT_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", "")
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
    else:
        REPLY_MESSAGE = None
