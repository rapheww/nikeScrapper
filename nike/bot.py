import discord
from discord.ext import commands
import os
import os
from dotenv import load_dotenv
from nike import run
from playwright.async_api import async_playwright
load_dotenv()

token_discord = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"Le bot {bot.user.name} est en ligne et prêt !")
    try:
        # Synchrone les commandes avec Discord (indispensable pour voir les /)
        synced = await bot.tree.sync()
        print(f"Nom de commandes Slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur de synchronisation : {e}")
        
@bot.tree.command(name="hello", description="Dit bonjour")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")

@bot.tree.command(name="nike_scrapping", description="Get the stock estimation of a pair")
async def scrapping(interaction: discord.Interaction, sku : str):
    await interaction.response.defer(thinking=True)
    async with async_playwright() as play:
        toSend = await run(pw=play, input=sku)
        await interaction.followup.send(embed=toSend)


bot.run(token_discord)