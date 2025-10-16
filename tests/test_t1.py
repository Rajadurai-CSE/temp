import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from feature1 import addition
from feature2 import subtraction

def test_add():
    assert addition(2, 3) == 5
    assert addition(-1, 5) == 4
    assert addition(0, 0) == 0

def test_subtract():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 5) == -5
    assert subtraction(-3, -3) == 0
