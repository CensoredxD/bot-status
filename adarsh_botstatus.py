
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import time
import psutil
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
                bot_uptime = int(time.time() - _boot_)
                cpu = psutil.cpu_percent(interval=0.5)
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage("/").percent
                UP = f"{get_readable_time((bot_uptime))}"
                CPU = f"{cpu}%"
                RAM = f"{mem}%"
                DISK = f"{disk}%"
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xyz_adarsh = f"📊 **<u>LIVE BOT STATUS</u>**\n\n**💬 {CHANNEL_OR_GROUP_TYPE}**: {CHANNEL_OR_GROUP_NAME}🚥"
                for bot in BOT_LIST:
                    try:
                        yyy_adarsh = await app.send_message(bot, "/start")
                        aaa = yyy_adarsh.message_id
                        await asyncio.sleep(5)
                        zzz_adarsh = await app.get_history(bot, limit = 1)
                        for ccc in zzz_adarsh:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xyz_adarsh += f"\n\n🤖 **BOT**: @{bot}\n**STATUS**: down 🔴"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xyz_adarsh += f"\n\n🤖 **BOT**: @{bot}\n**STATUS**: Up 🟢"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xyz_adarsh += f"\n\n🔷 Last checked on: {last_update} ({TIME_ZONE})\n\n<i>🔄 List is Updated every 1 Mins - Powered by @censored_xD \n Have a **Suggestion**  or want to report a **Bug**  \n  Contact at @censored_xD \n <i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xyz_adarsh)
                print(f"Last checked on: {last_update}🇮🇳")                
                await asyncio.sleep(60)
                        
app.run(main_adarsh())

