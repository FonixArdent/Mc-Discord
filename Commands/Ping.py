# Commands/Ping.py
from Commands._global_ import discord

@discord.app_commands.command(
    name="ping",
    description="🏓 Check the bot's latency",
)
async def ping_command(interaction: discord.Interaction):
    latency = round(interaction.client.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! Latency: {latency} ms", ephemeral=True)
