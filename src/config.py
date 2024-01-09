import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=os.path.join(BASE_DIR.parent, ".env"))


WEB_PORT = int(os.getenv("WEB_PORT"))
WEB_HOST = str(os.getenv("WEB_HOST"))

MONGODB_URL = str(os.getenv("MONGODB_URL"))
MONGODB_DATABASE = str(os.getenv("MONGODB_DATABASE"))
MONGODB_COLLECTION = str(os.getenv("MONGODB_COLLECTION"))
