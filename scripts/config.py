# Identifiants lus dans les variables d'environnement ou un fichier .env (jamais dans le code)
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

FTP_ip = os.getenv("FTP_IP")
FTP_user = os.getenv("FTP_USER")
FTP_pw = os.getenv("FTP_PW")

WAMP_username = os.getenv("WAMP_USERNAME")
WAMP_password = os.getenv("WAMP_PASSWORD")
WAMP_database = os.getenv("WAMP_DATABASE")
