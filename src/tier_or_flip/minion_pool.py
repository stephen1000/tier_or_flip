""" Minions """
import json
import random
from pathlib import Path
from collections import defaultdict

import requests

from tier_or_flip import settings

pool_path = Path(settings.DATA_DIR) / "minion_pool.json"


def fetch_minion_pool() -> dict:
    """ Fetch a new minion pool """
    minions = [
        minion
        for minion in requests.get(settings.CARD_DB_ENDPOINT).json()
        if minion.get("battlegroundsPremiumDbfId")
    ]
    pool = defaultdict(list)
    for minion in minions:
        pool[minion.get("techLevel")].append(minion)
    return pool


def save_minion_pool(pool: dict):
    """ Save the new minion pool to disk """
    pool_path.write_text(json.dumps(pool))


def update_minion_pool():
    """ Fetch and save a minion pool """
    pool = fetch_minion_pool()
    save_minion_pool(pool)
    return pool


def load_minion_pool() -> dict:
    """ Load the cached minion pool """
    return json.loads(pool_path.read_text())


def flip(tier: int) -> list:
    """ Fetch a sample of minions by tier """
    pool = load_minion_pool()
    n_to_show = tier // 2 + 3
    available_minions = []

    for t in range(1, tier + 1):
        for _ in range(settings.TIER_COUNTS[t]):
            available_minions += pool[str(t)]

    flip = []
    for _ in range(n_to_show):
        random.shuffle(available_minions)
        flip.append(available_minions.pop())
    return flip
    #      [
    #     available_minions.pop(random.randrange(len(available_minions)))
    #     for _ in range(n_to_show)
    # ]


if __name__ == "__main__":
    for tier in range(1,7):
        print(', '.join(minion['name'] for minion in flip(tier)))