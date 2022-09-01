
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_adarsh():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xyz_adarsh = f"📊 **<u>𝙇𝙞𝙫𝙚 𝙅𝙚𝙧𝙧𝙮𝙈𝙪𝙨𝙞𝙘𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙪𝙨</u>**\n\n**📡 {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}🚥"
                for bot in BOT_LIST:
                    try:
                        yyy_adarsh = await app.send_message(bot, "/start")
                        aaa = yyy_adarsh.message_id
                        await asyncio.sleep(5)
                        zzz_adarsh = await app.get_history(bot, limit = 1)
                        for ccc in zzz_adarsh:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xyz_adarsh += f"\n\n🤖 **𝘽𝙤𝙩**: @{bot}\n**STATUS**: down 🔴 Bot is down contact Bot owner"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xyz_adarsh += f"\n\n🤖 **𝙅𝙚𝙧𝙧𝙮𝙈𝙪𝙨𝙞𝙘𝘽𝙤𝙩**: @{bot}\n**STATUS**: 𝙱𝚘𝚝 𝚄𝚙[𝙻𝚒𝚟𝚎] ✅ & 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝚊𝚠𝚎𝚜𝚘𝚖𝚎 𝚠𝚒𝚝𝚑 𝚉𝚎𝚛𝚘 % 𝙻𝚊𝚐"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xyz_adarsh += f"\n\n🔷 Last checked on: {last_update} ({TIME_ZONE})\n\n<i>🔄 𝙎𝙩𝙖𝙩𝙪𝙨 𝙐𝙥𝙙𝙖𝙩𝙚 𝙖𝙪𝙩𝙤 𝙞𝙣 𝙚𝙫𝙚𝙧𝙮 5 𝙈𝙞𝙣𝙪𝙩𝙚𝙨 - 🅾🆆🅽🅴🆁 @Aditya_xDz \n <i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xyz_adarsh)
                print(f"Last checked on: {last_update}🇮🇳")                
                await asyncio.sleep(300)
                        
app.run(main_adarsh())

