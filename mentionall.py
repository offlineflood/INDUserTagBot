import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config 


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS


client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []
  

	
	
	
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**🤖Hello...{ad}💭,**\nMy Name is [𝐔𝐒𝐓𝐀 𝑇𝑎𝑔𝑔𝑒𝑟 𝘉𝑟](http://t.me/UstaTagbot)-u.\n**I have the authority to tag all members in your group.\n\ n🤖For more information, visit the '📚Commands' section.**", buttons=(
                     [Button.url('➕ Add me to a Group ➕','http://t.me/UstaTagbot?startgroup=a')],
	             [Button.inline(f"📚 Commandments", data="help"),
	              Button.inline(f"📑 Offers", data="reklam")],
	             [Button.url('Group💬', 'https://t.me/DejavuTeam'),
                      Button.url('𝐔𝐒𝐓𝐀 𝐁𝐎𝐓𝐋𝐀𝐑 👨‍💻', 'https://t.me/ustabots')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"** [𓆩𓄂𝙰𝚂𝚀🇦🇿 𝑇𝑎𝑔𝑔𝑒𝑟 𝘉𝘰𝘵](http://t.me/UstaTagbot)'un Əmrlər üçün?.Bot'a daxil olub.**", buttons=(
                     [Button.url('💡Switch to Bota','https://t.me/UstaTagbot?start=start')],
	             [Button.url('𝐔𝐒𝐓𝐀 𝐁𝐎𝐓𝐋𝐀𝐑 👨‍💻','https://t.me/ustabots'),
		      Button.url('Group💬', 'https://t.me/DejavuTeam')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**🤖Hello...💭,**\nMy Name is [𝐔𝐒𝐓𝐀 𝑇𝑎𝑔𝑔𝑒𝑟 𝘉𝑟](http://t.me/UstaTagbot)-u.\n**I have the authority to tag all members in your group.\n\ n🤖For more information, visit the '📚Commands' section.**", buttons=(
                     [Button.url('➕ Add me to a Group ➕','http://t.me/UstaTagbot?startgroup=a')],
	             [Button.inline(f"📚 Commandments", data="help"),
	              Button.inline(f"📑 Offers", data="reklam")],
	             [Button.url('Group💬', 'https://t.me/DejavuTeam'),
                      Button.url('𝐔𝐒𝐓𝐀 𝐁𝐎𝐓𝐋𝐀𝐑 👨‍💻', 'https://t.me/ustabots')],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"** [𝐔𝐒𝐓𝐀 𝑇𝑎𝑔𝑔𝑒𝑟 𝘉𝘰𝘵](http://t.me/UstaTagbot)-un Help '📚 Commands' These are.⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🤖➪ /tag <reason> - 5 Tag Shoots with.**\n**🤖➪ /etag <reason> - Tags with Emoji.**\n**🤖➪ /stag <reason> - Tags with Words.**\n**🤖 ➪ /tektag <reason> - Individual tags with members.**\n**🤖➪ /master <reason> - Tag tags related to master Tag Bot.**\n**🤖➪ /admins <reason> - Admins Individual tags.**\n**🤖➪ /cancel - Stop Tag Filtering.**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
	             [Button.url('Group💬', 'https://t.me/DejavuTeam'),
                      Button.url('𝐔𝐒𝐓𝐀 𝐁𝐎𝐓𝐋𝐀𝐑 👨‍💻', 'https://t.me/ustabots')],
	             [Button.inline(f"🔙 Back", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**📌 You can contact the owner for offers...**", buttons=(
		     [Button.url('🎉 Owner', 'https://t.me/MUCVE_M')],
	             [Button.url('Group💬', 'https://t.me/DejavuTeam'),
                      Button.url('𝐔𝐒𝐓𝐀 𝐁𝐎𝐓𝐋𝐀𝐑 👨‍💻', 'https://t.me/ustabots')],
	             [Button.inline(f"🔙 Back", data="start")]
                    ),
                    link_preview=False)
	
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**This command is valid for groups!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Only administrators can use this command!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**I Can Reply to Previous Messages! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**There is no reason to start! **")
  else:
    return await event.respond("**Write a reason to start the tag...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag operation successfully terminated!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**This command is valid for groups! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Only administrators can use this command! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**I Can Reply to Previous Messages! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**There is no reason to start! **")
  else:
    return await event.respond("**There is no reason to start, write...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag operation successfully terminated! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**This command is valid for groups! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Only administrators can use this command! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**I Can Reply to Previous Messages! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**There is no reason to start! **")
  else:
    return await event.respond("**There is no reason to start, write...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**↯ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Operation Stopped Successfully! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Operation Stopped Successfully! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"Some people feel the rain, others just get wet,"
"Remember; Not everyone who comes loves.. And no lovers leave",
"No soul's pain is less than yours",
"I try everything; but I do what I can.",
"Love is the whole story of a woman's life and the only adventure of a man.",
"Happiness is first of all in physical health.",
"It's not how long we live, it's how we live"
"Earth is a rainbow, mind is a prism, and existence is a white ray.",
"If you don't know where you're going, it doesn't matter which way you go.",
"It's the most precious time in life. Be careful who you give a gift to.",
"You can't break all the windows in the house and then knock on the door.",
"Happiness is not in the way you live, but in the way you look at life.",
"Remember; Not everyone who comes loves.. And no lovers leave.",
"Half a breath in this life. Plan nothing but love...",
"I wish everyone a life as good as the good in them.",
"What makes beauty beautiful is decency, and decency is the reason to love beauty!",
"The fragrance of the rose remains in the hands of the one who gives the rose."
"What you seek is what seeks you.",
"Even a bird flaps its wings in the sky.",
"Life is not entrusted to those who do not know how to take heart.",
"Don't be afraid to be honest, you will lose the most to the wrong people.",
"A person is not a tree, when it breaks you make a sound.",
"Learning is the only proof of life.",
"As the world's population increases, the number of people decreases.",
"Never tell the truth to people you don't think deserve it.",
"Thank goodness the sky doesn't fit in any wallet yet.",
"Be yourself. Everyone has already taken it.",	
"I was hurt, I swallowed the lumps in my throat.",
"She smiled so beautifully that if I didn't love her, it would be in vain.",
"I'm not the one he loves. I can't tell you the pain of this.",
"I'm not the one he loves. I can't tell you the pain of this.",
"You get used to everything with time, but it doesn't end.",
"If you tell the truth, you don't need to remember anything.",
"Be the first to tell the truth... Otherwise, someone will definitely tell the truth instead of you.",
"Men may be stronger, but women are resilient.",
"There is no prescription for pain,"
"All dreams can come true if you have the courage to pursue them.",
"This is a secret love, I can't tell anyone about my troubles.",
"Do you think love forgives everything?",
"You and I need a cigarette"
"I didn't know anyone special than you,"
"One day love ends, memories remain"
"Love is such a long word!",
"You are the most memorable thing I remember.",
"There are people I miss laughing with.",
"The one who finds happiness in you is yours, moreover, the guest.",
"Love a lot, but if you don't like it, don't force it!"
"She laughed so beautifully that it would be a shame if I didn't love her.",
"and a man should be a companion to a man and heal his wounds",
"The graveyard is full of those who regret the nerve",
"Love is like the wind, you can't see it, but you can feel it."
"there is a scale, there is a measure, there is a time for everything",
"Don't be fooled by innocent looks, some of them are given a standing ovation by the devil...",
"life is not long enough to wait for tomorrow",
"The good never lose, they are lost."
"I hope you don't need the love you've been missing",
"I wish you would give peace instead of reason",
"I really miss that smell I never knew",
)	

@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**This command is valid for groups! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Only administrators can use this command! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**I Can Reply to Previous Messages! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**There is no reason to start! **")
  else:
    return await event.respond("**There is no reason to start, write...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully!**")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎Adminlər Siyahısı♕︎"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ↯ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/master ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**This command is valid for groups! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Only administrators can use this command! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**I Can Reply to Previous Messages! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**There is no reason to start! **")
  else:
    return await event.respond("**There is no reason to start, write...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Operation Stopped Successfully! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

usta = ('Who is this?','🙄👉🤲Aagil','🙄 Did you do what I said? 😐','My life is full 🥲 nassin😍','Why are you looking at me like that? 🌝','I d rather not be in the plan than be in the second plan. 🎯','I ve seen you in other groups','When youre hungry, you re not you','Why do you lie, the person has a bed on his head','Hajji, how are you? You don t like it','They say you re dead🤔','My strength... Because I have no other choice, I know I won t be able to catch you if I fall...🚬','Let s love each other until the back streets end❤️','Corona grew like this, you didn t grow','corona I couldn t forget you like this,','how many consonants are there in the word I love you','why do boys live less','do plants die when they get old or because of neglect','are you still drinking tea in hot weather','may God bless you','come soon our gift competition has started','My dreams live as long as a butterfly s life 💔🥀','I m going to look at the flowers from below..➰','For a silent woman... you are a lost man.! 🖤','Don t trust me, don t trust me.','You need to be strong more than me, because somewhere in your heart you know you are wrong.🤙','Makeup and face paints. The roads are beautiful, but sewer under it.👋😉 ',' 𝙸𝙸𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗𝚌𝚎𝚔𝚜𝚌𝚎𝚔𝚜𝚌𝚎𝚔𝚜𝚍a 𝚑𝚎𝚌𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚔𝚒𝚖𝚒𝚔𝚒𝚖𝚒𝚌𝚎𝚔𝚜𝚌𝚎𝚔𝚜𝚍a 𝚑𝚎𝚌𝚗𝚒𝚟𝚊𝚡𝚝 𝚟𝚊𝚡𝚝 𝚘𝚕 𝚍𝚎𝚢 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚊𝚖𝚖𝚊𝚗𝚒𝚗𝚒𝚗𝚒 𝚌 𝚌 𝚌 𝚚𝚘𝚢𝚖𝚊𝚐̆𝚚𝚘𝚢𝚖𝚊𝚐̆𝚖𝚒𝚛𝚖𝚒𝚛𝚜𝚜𝚗𝚒𝚗𝚒𝚍 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 𝚌 there are people.🔥😂','I can t find the things I put in their place. I put some of them in people s place, now come find it and see how you find it✊','Let someone take it 🫢','If you can t find your match in this life, don t be upset, then you are a matchless match. Gabriel García Márquez (Mexican writer)🥲',' Welcome Nafas🥲','You re not coming Baby😒','Who are you writing to??? 🤨','Come Ugly Boy😌','My Chocolate😍','Oh You re Here 😳','Buy You Chocolate🤓👉🍫','Don t You Love Me?🙁 Then Be 🙂','Oh Are You Right?🧐',' Who s This😁','Come Fight 😁💪','Look What I Got You😌👉🐒','You re Beautiful🤢 Ugly Duckling','Who Are You🙄A Geda👀','Come I ve Got You 🤫',' Ooo You re so beautiful🤌🤐Honey','Private 😌doonbalah','Come see me yet🧐 What did you say to me😬','Shame on you😫 Why don t you write😑','I m sick of you🥲','How much is this✌️🙂','Your number send me a message on Vp🙊','👉👀 Get your eyes off come on😒','ummm Lets do yoga🧘‍♀🤭','come let me lick you😪🍻','Take my mind off my head😵‍💫come to me',' I saw you my daughter when you got up 🤒',) 


@client.on(events.NewMessage(pattern='/offline'))
async def handler(event):
    # Kimsə "Salam" və başqa bir şey deyəndə cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sən mənə sahib deyilsən!__")
    await event.reply('**Bot Working Dont worry ** \n https://t.me/DegGixM \n\n╭━━━╮ \n╰╮╭╮┃╱╱╭╮\n╱┃┃┃┣━━╋╋━━┳╮╭┳╮╭╮\n╱┃┃┃┃┃━╋┫╭╮┃╰╯┃┃┃┃\n╭╯╰╯┃┃━┫┃╭╮┣╮╭┫╰╯┃\n╰━━━┻━━┫┣╯╰╯╰╯╰━━╯\n╱╱╱╱╱╱╭╯┃\n╱╱╱╱╱╱╰━╯',
		     buttons=(
	             [Button.url('DegGixM','https://t.me/DegGixM'),
	             Button.url('Ali','https://t.me/MUCVE_M')],
                    ),
                    link_preview=False)

print(">> Don't worry the bot is working. @MUCVE_M For information <<")
client.run_until_disconnected()
