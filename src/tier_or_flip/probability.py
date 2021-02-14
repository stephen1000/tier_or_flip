""" Calculate odds """
from typing import List, Optional
from minion_pool import flip


def flip_for_minions(
    minions: List[str],
    tier: Optional[int] = None,
    turn: Optional[int] = None,
    flips: Optional[int] = None,
    sellable: Optional[int] = None,
) -> int:
    """ Simulate a number of flips """
    if turn and not flips:
        flips = min((turn + 2, 10)) - 3

    if sellable:
        flips += sellable

    for flip_num in range(flips + 1):
        offered = flip(tier)
        for minion in offered:
            if minion["name"] in minions:
                return flip_num
    return -1


def get_odds(
    minions: List[str],
    simulations: Optional[int] = 1000,
    tier: Optional[int] = None,
    turn: Optional[int] = None,
    flips: Optional[int] = None,
    sellable: Optional[int] = None,
):
    """ Get odds of rolling at least 1 of ``minions`` """
    passes = 0
    fails = 0
    for _ in range(simulations):
        if flip_for_minions(minions, tier, turn, flips, sellable) >= 0:
            passes += 1
        else:
            fails += 1

    return float(passes) / (passes + fails)


if __name__ == "__main__":
    print(get_odds("Alleycat", flips=2, tier=2))