import os
from telebot import TeleBot
from shazamio import Shazam

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(TOKEN)
shazam = Shazam()

@bot.message_handler(content_types=['audio', 'voice', 'video'])
def get_song(message):
    file_info = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("temp.mp3", "wb") as f:
        f.write(downloaded_file)
    out = shazam.recognize_song("temp.mp3")
    track = out['track']
    title = track['title']
    artist = track['subtitle']
    bot.reply_to(message, f"এই গানটা হলো: {title} — {artist}")

bot.polling()
