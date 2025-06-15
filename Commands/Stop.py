# Commands/Stop.py
from Commands._global_ import asyncio
from Commands._global_ import discord
from Commands._global_ import if_dev

@discord.app_commands.command(
    name="stop",
    description="🛑 Stops the bot (dev only)",
)
@if_dev()
async def stop_command(interaction: discord.Interaction):
    await interaction.response.send_message("🛑 Stopping the bot...", ephemeral=True)
    
    await interaction.client.change_presence(
        status=discord.Status.dnd,
        activity=discord.CustomActivity(
            f"⚠️ {interaction.client.application.name} is stopping by developer request [ {interaction.user.display_name} ]"
        )
    )

    await asyncio.sleep(5)

    await interaction.followup.send("✅ Bot stopped successfully", ephemeral=True)
    await interaction.client.close()
