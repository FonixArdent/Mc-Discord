from discord import app_commands

DEVELOPERS = [994927811049574431]  # Remplace par ton ID

def if_dev():
    def predicate(interaction):
        return interaction.user.id in DEVELOPERS
    return app_commands.check(predicate)
