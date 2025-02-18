import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "25494342"))
API_HASH = getenv("API_HASH", "417cd441a3e027226e7a1333b2ea4ea0")
BOT_TOKEN = getenv("BOT_TOKEN", "7995627013:AAEd-MdITChEE9RwNejtP60jkMoA2MnAEd0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgAZiHdAd4EOX2_TFaotq0BvHmvyfNnuzW1BXj_K4vIjrDbv_c2Ii7HvAyDU-kjCHAQsEvvY-AsNtiGCQ000WasBQ6qvB4wV5Ez7XZQyNmqbe2Cyg0DUTLHGFqKx-cuZ6RuYIla3TFYNx02fRE1TK_cYmdZr2KC4PvH80JM_zSzCju99osQ8xTQGI7L4wsZmOGD7ACCZpbGt_3WM-nalZCq4gS37ubEmu1pCLc7GE5NVkyUYyG1fERP8LRisXehFuf5Ly-ZOZ8e98sr0tYBRKfLsTODFsGVWRVIYvyZ4KstWO9O54MAm5eKkasktNoBSv49KSMPiBrtmbiNFKBXTi8loAAAAAVYfLGoA")
BOT_USERNAME = getenv("BOT_USERNAME", "Botmuozknet_bot")
COMMAND_PREFIXES = list(getenv("VIP_Netrogen", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7423822482").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "7423822482").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "AL_AGER")
GROUP = getenv("GROUP", "AL_AGER")
BOT_NAME = getenv("BOT_NAME", "Music music ")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


