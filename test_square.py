import pytest
from square import get_square

def test_sq():
    assert get_square(2) == 4
    assert get_square(3) == 9
    assert get_square(4) == 16

def test_str():
    with pytest.raises(TypeError):
        get_square('cat')