from Commands._global_ import discord
import json
import os

@discord.app_commands.command(name="removechat", description="❌ Mark a channel as removed from Minecraft chat")
async def remove_chat_command(interaction: discord.Interaction, channel: discord.TextChannel):
    """Replace a channel in 'linked_channels' with an ID marked as removed"""

    path = "data/channels.json"

    if not os.path.exists(path):
        await interaction.response.send_message("⚠️ The channels.json file does not exist.", ephemeral=True)
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        await interaction.response.send_message("❌ The JSON file is corrupted.", ephemeral=True)
        return

    linked_channels = data.get("linked_channels", [])
    channel_class = data.get("channel", [])
    channel_id = channel_class.get("channel_id", [])

    if str(channel.id) not in linked_channels:
        await interaction.response.send_message(f"❌ The channel {channel.mention} is not linked.", ephemeral=True)
        return

    # Remove from the list and add as ID = "removed"
    linked_channels.remove(str(channel.id))
    data["linked_channels"] = linked_channels
    data[str(channel.id)] = "removed"

    # Save
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    await interaction.response.send_message(
        f"✅ The channel {channel.mention} has been marked as **removed**.", ephemeral=True
    )
