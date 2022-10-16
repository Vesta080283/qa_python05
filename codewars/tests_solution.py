from solution import *


def basic_tests():
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    print(are_you_playing_banjo("martin"))
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
    assert are_you_playing_banjo("rolf") == "rolf plays banjo"
