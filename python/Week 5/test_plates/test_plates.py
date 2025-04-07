from plates import is_valid

def test_plates():
    assert is_valid("A2") == False
    assert is_valid("zu#kk") == False

def test_length():
    assert is_valid("AAAAAAA") == False

def test_number_placement():
     assert is_valid("cs50as") == False

def test_zero_placement():
    assert is_valid("CS05") == False
