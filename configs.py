# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27693415"))
    API_HASH = getenv("API_HASH", "8dc020d35ff99813b494f20955d8c724")
    BOT_TOKEN = getenv("BOT_TOKEN", "8455094377:AAGcAPZ0KPOrMHX3MRu5Al2NULnpOl4xcMA")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002816736360")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "8115758627").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ledaxad522:FiJVewcu6tkNBN2q@cluster0.cealr1i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
