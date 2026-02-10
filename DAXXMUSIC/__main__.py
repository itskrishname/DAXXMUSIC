import asyncio
import importlib
import os
import httpx

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DAXXMUSIC import LOGGER, app, userbot
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.misc import sudo
from DAXXMUSIC.plugins import ALL_MODULES
from DAXXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def save_cookies():
    if config.COOKIES_URL:
        try:
            url = config.COOKIES_URL
            # Automatically convert batbin/pastebin links to raw if needed
            if "batbin.me" in url and "raw" not in url:
                url = url.replace("batbin.me/", "batbin.me/raw/")
            elif "pastebin.com" in url and "raw" not in url:
                url = url.replace("pastebin.com/", "pastebin.com/raw/")

            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()

                cookies_dir = "cookies"
                if not os.path.exists(cookies_dir):
                    os.makedirs(cookies_dir)
                else:
                    # Clean up existing cookies to avoid using stale ones
                    for filename in os.listdir(cookies_dir):
                        if filename.endswith(".txt"):
                            os.remove(os.path.join(cookies_dir, filename))

                with open(os.path.join(cookies_dir, "cookies.txt"), "w") as f:
                    f.write(response.text)
                LOGGER(__name__).info(f"Cookies fetched successfully from {url}")
        except Exception as e:
            LOGGER(__name__).error(f"Failed to fetch cookies: {e}")


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await save_cookies()

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DAXXMUSIC.plugins" + all_module)
    LOGGER("DAXXMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DAXXMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝐌ᴀx 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("DAXXMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝐌ᴀx\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DAXXMUSIC").info("𝗦𝗧𝗢𝗣 𝐌ᴀx 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
