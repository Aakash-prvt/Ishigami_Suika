#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Sabka Malik : <a href='tg://user?id={OWNER_ID}'>@Call_Me_Blank</a>\n○ Visit this too : @WebCinematics\n○ Channel : @Otaku_Library \n○ Support Group : @Otaku_Chats \n○ Harem Animes at : @Harem_Library  \n○ Hanimes at : @Hanime_Library2</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
