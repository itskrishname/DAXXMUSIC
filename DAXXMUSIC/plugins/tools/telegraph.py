import requests
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto

def upload_file(path):
    try:
        with open(path, 'rb') as f:
            files = {'fileToUpload': f}
            data = {'reqtype': 'fileupload'}
            response = requests.post('https://catbox.moe/user/api.php', files=files, data=data)

        if response.status_code == 200:
            return response.text
        else:
            return False
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

@app.on_message(filters.command(["tgm" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
        path = reply.download()
        url = upload_file(path)
        if url:
            i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
        else:
            i.edit("Failed to upload file.")
    else:
        message.reply("Please reply to a media file.")

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul_graph(_, message):
    reply = message.reply_to_message
    if reply and reply.media:
        i = message.reply("𝐌𝙰𝙺𝙴 𝐀 𝐋𝙸𝙽𝙺...")
        path = reply.download()
        url = upload_file(path)
        if url:
            i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}')
        else:
            i.edit("Failed to upload file.")
    else:
        message.reply("Please reply to a media file.")
