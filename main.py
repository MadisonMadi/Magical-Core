from discord import app_commands, Intents, Client, Interaction
from Commands.info_command import on_message
from Restarter.keep_alive import keep_alive

import discord
import os


class Executive(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


client = Executive(intents=Intents.all())


async def _init_command_response(interaction: Interaction) -> None:
    await interaction.response.send_message("\n".join([
        f"Hi **{interaction.user}**, thank you for saying hello to me."]))


@client.tree.command()
async def hello(interaction: Interaction):
    """Says hello or something"""
    await _init_command_response(interaction)


client.event(on_message)

keep_alive()

try:
    client.run(os.getenv("token"))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system('kill 1')
    os.system("python restarter.py")