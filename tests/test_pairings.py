import pairings

def test_ordered_by_player():
    history = [
        {'pairing': [], 'result': []}
    ]
    new = pairings.by_player(history)
    assert new[1] != None
