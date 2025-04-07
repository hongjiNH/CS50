from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/100") == 1

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_labelingpercent():
    assert gauge(25) == "25%"

def test_labeling1():
    assert gauge(1) == "E"

def test_labeling99():
    assert gauge(99) == "F"
