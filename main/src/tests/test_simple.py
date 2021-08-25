import pytest

from app.main import add_3, div_int


def test_add_3():
    assert add_3(5) == 8


def test_exception():
    with pytest.raises(ZeroDivisionError):
        res = div_int(1, 0)
