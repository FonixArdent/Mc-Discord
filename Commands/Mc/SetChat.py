from Commands._global_ import discord
import json

@discord.app_commands.command(name="setchat", description="👾 Set the chat for detecting messages")
async def set_chat_command(interaction: discord.Interaction, channel: discord.TextChannel):
    """Set the channel for detecting messages."""

    await interaction.response.send_message(f"👾 Chat channel set to {channel.mention}", ephemeral=True)

    # Stocker l'ID du salon
    with open("data/channels.json", "w", encoding="utf-8") as f:
        json.dump({
            "channel": {
                "channel_id": channel.id,
                "channel_name": channel.name
            },
            "server": {
                "server_name": interaction.guild.name
            }
        }, f, indent=4)

    await interaction.client.change_presence(activity=discord.Game(name=f"Listening in {channel.name}"))
