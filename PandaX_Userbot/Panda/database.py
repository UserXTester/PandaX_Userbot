from decouple import config
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    SESSION = config("SESSION", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    VC_PLUGIN = config("VC_PLUGIN", default="player")
    MODULES = config("MODULES", default=None)


REDISHOST = config("REDISHOST", default=None)
REDISPORT = config("REDISPORT", default=None)
REDISUSER = config("REDISUSER", default=None)
