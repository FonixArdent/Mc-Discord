# Commands/Clear.py
from Commands._global_ import discord
from Commands._global_ import if_dev

@discord.app_commands.command(
    name="clear",
    description="🧹 Deletes all commands in the guild", # you can also remove this if you want it to be global
)
@if_dev()
async def clear_command(interaction: discord.Interaction):
    await interaction.response.send_message("🧹 Clearing commands... (dev only)", ephemeral=True)

    try:
        interaction.client.tree.clear_commands(guild=interaction.guild)
        await interaction.client.tree.sync(guild=interaction.guild)

        await interaction.followup.send("✅ All commands have been successfully deleted!", ephemeral=True)

        await interaction.client.change_presence(
            status=discord.Status.online
        )
    except Exception as e:
        await interaction.followup.send(f"❌ Error: {e}", ephemeral=True)
