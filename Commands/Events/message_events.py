import json
from discord.ext import commands
import discord
import unicodedata
import os
import re


# Load channel data
def load_channel_id():
    try:
        with open("data/channels.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return str(data["channel"]["channel_id"])
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return None

def load_server_name():
    try:
        with open("data/channels.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["server"]["server_name"]
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return None

def load_channel_name():
    try:
        with open("data/channels.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["channel"]["channel_name"]
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        return None


class MessageListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = load_channel_id()
        self.server_name = load_server_name()
        self.channel_name = load_channel_name()


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        # If the message is from a bot or not in the specified channel, ignore it
        if message.author.bot or str(message.channel.id) != self.channel_id :
            return


        def clean_content( text: str) -> str:
        # 1. Remove accents (é → e, à → a)
            text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

        # 2. Remove all special characters except letters, numbers, space, comma, and period
            text = re.sub(r"[^a-zA-Z0-9\s,\.]", "", text)

        # 3. Clean up multiple spaces
            text = re.sub(r"\s+", " ", text).strip()

            return text



        # Format the message
        data = {
            "server": self.server_name,
            "channel": message.channel.name,
            "username": message.author.display_name,
            "content": clean_content(message.content)
        }

        # Write to a file that your datapack can read

        try:

            os.makedirs("mc_bridge", exist_ok=True)

            with open("mc_bridge/latest_message.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"💬 Message sent to datapack: {data}")

        except Exception as e:
            print(f"❌ Error writing message: {e}")
