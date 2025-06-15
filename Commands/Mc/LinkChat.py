# Commands/LinkChat.py
import json
from Commands._global_ import discord
import asyncio

@discord.app_commands.command(name="linkchat", description="🔗 Enable message synchronization with Minecraft")
async def link_chat_command(interaction: discord.Interaction):
    await interaction.response.send_message("🔄 Loading linked channels...", ephemeral=True)

    try:
        with open("data/channels.json", "r") as f:
            data = json.load(f)

        channels = data.get("linked_channels", [])

        if str(interaction.channel.id) in channels:
            await interaction.followup.send("✅ This channel is already linked to Minecraft.", ephemeral=True)
        else:
            channels.append(str(interaction.channel.id))
            data["linked_channels"] = channels

            with open("data/channels.json", "w") as f:
                json.dump(data, f, indent=4)

            await interaction.followup.send("🔗 This channel is now synchronized with Minecraft!", ephemeral=True)
            await interaction.channel.edit(slowmode_delay=60)
            await interaction.followup.send("🔄 The bot must be restarted for all changes to take effect. and then run `/linkchat`", ephemeral=False)

    except Exception as e:
        await interaction.followup.send(f"❌ Error: {e}", ephemeral=True)
