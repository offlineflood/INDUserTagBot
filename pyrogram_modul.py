from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton #düyməsi yoxdur.!
import pyrogram
from Config import Config
from datetime import datetime
from telethon import Button


app = Client(
    "User Tag Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

#---------------------------------------------------------------GROUP GIREKEN SALAMLAMA MSJ------------------------------------------------------------------------------#
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Hello` {msg.from_user.mention} `Me` {msg.chat.title} `Thanks for adding to the group⚡️` \n\n **🤖I was created to tag users in groups.\n🤖 Just type /start for help.✨**''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#
        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('🤖 [𝐔𝐒𝐓𝐀 𝑇𝑎𝑔𝑔𝑒𝑟 𝘉𝑟](https://t.me/UstaTagbot) Joined The Group.\n Welcome Owner, How are you?🥰.')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

app.start()
print(f"Bot started with pyrogram ({pyrogram.__version__}... Start the bot!")
idle()
