from dotenv import load_dotenv
import os

load_dotenv()


CARD_DB_ENDPOINT = os.getenv("CARD_DB_ENDPOINT")
DATA_DIR = os.getenv("DATA_DIR")

TIER_COUNTS = {
    1: 16,
    2: 15,
    3: 13,
    4: 11,
    5: 9,
    6: 7,
}


if not CARD_DB_ENDPOINT:
    raise Exception(f"Required setting not set- 'CARD_DB_ENDPOINT'")
if not DATA_DIR:
    raise Exception(f"Required setting not set- 'DATA_DIR'")
