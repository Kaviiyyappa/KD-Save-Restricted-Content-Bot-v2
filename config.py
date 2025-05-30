# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "21939922"))
API_HASH = getenv("API_HASH", "bd2d18dd26b200480bda4cbdf2c2da30")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6757014146").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://KD-Save-Restricted-Content-Bot-v2:injEhJ90EpRSraB0@kd-save-restricted-cont.726qafr.mongodb.net/?retryWrites=true&w=majority&appName=KD-Save-Restricted-Content-Bot-v2")
LOG_GROUP = getenv("LOG_GROUP", "-1002596050174")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002647873103"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "solourl.solofm.fun")
AD_API = getenv("AD_API", "fe670610a017289b8da3cc2f9d79805257029bd7")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
