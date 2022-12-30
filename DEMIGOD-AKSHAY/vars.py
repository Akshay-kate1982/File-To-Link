# (c) DEMIGOD-AKSHAY
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('21560317'))
    API_HASH = str(getenv('c171065f7c42504884ebf768329cbfae'))
    BOT_TOKEN = str(getenv('5910151104:AAEr2bsDYBXWPPwVM7N6gjrH6ysXoKIaIM4'))
    name = str(getenv('SESSION_NAME', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('-1001816089963'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('DEMIGOD-AKSHAY'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('FileToLink'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.railway.app'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('DEMIGOD_TRICKY', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
