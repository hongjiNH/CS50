import pytest
from seasons import diff

def test():

    with pytest.raises(SystemExit, match="Invalid"):
        diff("Januar 6th, 1998")


