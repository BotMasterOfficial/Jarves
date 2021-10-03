# Copyright (C) 2020-2021 by @BotMasterOfficial, < https://github.com/BotMasterOfficial >.
#
# This file is part of < https://github.com/BotMasterOfficial/Jarves > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/BotMasterOfficial/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import filters

from Jarves.pyrogramee.pluginshelper import admins_only, get_text
from Jarves import pbot


@pbot.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = get_text(message)
    if not sh:
        sh = "Hi!"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")


__mod_name__ = "♻️ 𝐓𝐚𝐠𝐚𝐥𝐥 ♻️"
__help__ = """
- /tagall : Tag everyone in a chat
"""
