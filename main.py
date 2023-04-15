import os
import discord
from discord import ApplicationCommand, InteractionResponseType
from discord.ext import commands
from Commands.info_command import on_message
from Restarter.keep_alive import keep_alive

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)


async def _init_command_response(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(
        f"Hi **{interaction.user}**, thank you for saying hello to me."
    )


@bot.slash_command(name="hello", description="Says hello or something")
async def hello(ctx: commands.Context):
    await _init_command_response(ctx)


bot.event(on_message)

keep_alive()

try:
    bot.run(os.getenv("token"))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("kill 1")
    os.system("python restarter.py")