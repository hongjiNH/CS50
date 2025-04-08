from um import count

def test_um():
    assert count("um, lol, UM lol") == 2
    assert count("um, yummmmy") == 1
