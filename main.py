import discord
import os

from dotenv import load_dotenv

from discord.ext import commands

from Commands.Ping import ping_command as ping
from Commands.Stop import stop_command as stop
from Commands.Clear import clear_command as clear

from Commands.Mc.SetChat import set_chat_command as set_chat
from Commands.Mc.LinkChat import link_chat_command as link_chat
from Commands.Mc.RemoveChat import remove_chat_command as remove_chat

from Commands.Events.message_events import MessageListener



# Load environment variables
load_dotenv("data.env")
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

# Intents Configuration
intents.guilds = True  
intents.typing = False

intents.message_content = True  

intents.members = True  
intents.messages = True  

# Guild ID for syncing commands 
GUILD_ID = discord.Object(id=1142421218151120916)

bot = commands.Bot(command_prefix="*", intents=intents)

@bot.event
async def on_ready():
    print(f"\n✅ Connected as {bot.user}")

    synced = await bot.tree.sync(guild=GUILD_ID)

    try:
        print(f"\n🌐 {len(synced)} commands synced")
    
    except Exception as e:
        print(f"\n❌ Sync Error: {e}")
    
    await bot.add_cog(MessageListener(bot))

    print(f"\n👋 {bot.user.name} is ready to receive commands!\n")

# Slash Commands Registration

bot.tree.add_command(ping, guild=GUILD_ID)
bot.tree.add_command(stop, guild=GUILD_ID)
bot.tree.add_command(clear, guild=GUILD_ID)

bot.tree.add_command(set_chat, guild=GUILD_ID)
bot.tree.add_command(link_chat, guild=GUILD_ID)
bot.tree.add_command(remove_chat, guild=GUILD_ID)


bot.run(TOKEN)