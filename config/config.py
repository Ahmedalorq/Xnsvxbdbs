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

API_ID = int(getenv("API_ID", "24900691"))
API_HASH = getenv("API_HASH", "c145460d9df00cd70aa75070982297a9")
BOT_TOKEN = getenv("BOT_TOKEN", "7686027992:AAETcz16tqCUEOtXpYHBTsHpk4ipV6f8mpE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgAlFchwpiOUfhJAmqcOPdZFdWKcZ7eJdwq1Zfq7so1rX6pz7o8QBPBocJzWXBdalE33fjveWBNzg_xtgtbGV1QGGT6X53-2rG3f-hWyOK_GXYhQoPn3_3yFzOOUOWCPt5ahNd0Y7DK7Uqx8Cd9Ui-bkECOSGZwWQKT41Z3ehOPGNhPwuONEE0I5o0nGZJeBekg6YAx8JAA4QRthUdLcIB7_g_-HPMJXilWDW7myOshsO0wvwxbPXtLGvclkmFQculmY0OnWcMQgFUasuRDlT6lmv4asGFZ84yV4c0xi9ZFVHfRfrBsKgDDAQRVcAx8NYOGf1rBLOxmkPyUUj_Omgnb2AAAAAXSr_QwA")
BOT_USERNAME = getenv("BOT_USERNAME", "Miozekbot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6252395788").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6252395788").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001975200806")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "televenom")
GROUP = getenv("GROUP", "televenom")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


