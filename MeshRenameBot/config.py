from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://saitama:Arox321@cluster0.6pwnrr4.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "764cb1c8d044fd73dfd61e363594d0ed"]
        API_ID = [int, 29357686]
        BOT_TOKEN = [str, "bot:6091779768:AAHP8D_xA-WbCygiBDyyjkTqRvAVZ9JpEPM"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 50]
        SLEEP_SECS = [int, 0]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, @Saitama_OnePunchMan_0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/Anime_lover_chats"]
        FORCEJOIN_ID = [int,5862168163]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
