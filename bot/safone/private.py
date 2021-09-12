
import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "👋🏻 **Hi [{}](tg://user?id={})**, \n\nI'm **Video Streaming bot**. \nI Can Stream Lives, Radios, YouTube Videos & Telegram Video Files On Voice Chat Of Telegram Channels & Groups 😉! \n\n**Made With ❤️ By @monstar_0!** 👑"
HELP_TEXT = """
🏷️ --**Setting Up**-- :

\u2022 Start a voice chat in your channel or group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Use /stream [youtube link] or /stream [live stream link] or /stream as a reply to a video file.

🏷️ --**Common Commands**-- :

\u2022 `/start` - start the bot
\u2022 `/help` - show help message

🏷️ --**Admin Only Commands**-- :

\u2022 `/radio` - start streaming the radio
\u2022 `/stream` - start streaming the video
\u2022 `/endstream` - stop streaming the video

© **Powered By** : 
**@StylishUser | @Monstar_0** 👑
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/STylishUser"),
            ],
            [
                InlineKeyboardButton("Owner", url="https://t.me/Tithonus"),
                InlineKeyboardButton("SOURCE CODE", url="https://github.com/MohsinHsn/Stream_video"),
            ],
            [
                InlineKeyboardButton("BACK HOME", callback_data="home"),
                InlineKeyboardButton("CLOSE MENU", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("SEARCH INLINE", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/StylishUser"),
            ],
            [
                InlineKeyboardButton("Owner", url="https://t.me/Tithonus"),
                InlineKeyboardButton("SOURCE CODE", url="https://github.com/mohsinhsn/Stream-video"),
            ],
            [
                InlineKeyboardButton("❔ HOW TO USE ❔", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("SEARCH INLINE", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/StylishUser"),
            ],
            [
                InlineKeyboardButton("Owner", url="https://t.me/tithonus"),
                InlineKeyboardButton("SOURCE CODE", url="https://github.com/mohsinhsn/Stream-video"),
            ],
            [
                InlineKeyboardButton("❔ HOW TO USE ❔", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/EnglishChatting_Club"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/StylishUser"),
            ],
            [
                InlineKeyboardButton("Owner", url="https://t.me/tithonus"),
                InlineKeyboardButton("SOURCE CODE", url="https://github.com/mohsinhsn/Stream-video"),
            ],
            [
                InlineKeyboardButton("❔ HOW TO USE ❔", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
