# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23160456"))
    API_HASH = getenv("API_HASH", "16f2fa81daef2829373070393b42a003")
    BOT_TOKEN = getenv("BOT_TOKEN", "6742451780:AAHP2H-qrGVFdvbdHby5v03LXGZ2hedqG4E")
    FSUB = getenv("FSUB", "Official_InstaPLUS")
    CHID = int(getenv("CHID", "-1001711008160"))
    SUDO = list(map(int, getenv("SUDO", "6367495275").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
