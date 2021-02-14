""" CLI """
import argparse
from tier_or_flip import minion_pool


def get_args():
    """ Gather arguments """
    parser = argparse.ArgumentParser(description="Tier or Flip CLI")
    parser.add_argument("command", choices=['update'], help="Command to run")
    return parser.parse_args()

def handle():
    args = get_args()
    if args.command == 'update':
        minion_pool.update_minion_pool()