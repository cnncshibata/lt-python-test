from typing import Union
import pytest

from app.main import grade


TEST_PARAMETERS = [
    (-1, Exception()),
    (0, 'C'),
    (39, 'C'),
    (40, 'B'),
    (59, 'B'),
    (60, 'A'),
    (79, 'A'),
    (80, 'S'),
    (100, 'S'),
    (101, Exception()),
]


# grade 関数の境界値分析を parametrize を使わずに書くと一度目の失敗でテストが止まってしまう
def test_grade_without_parametrize():
    raise_exception = [param for param in TEST_PARAMETERS if isinstance(param[1], Exception)]
    not_raise_exception = [param for param in TEST_PARAMETERS if param not in raise_exception]
    for score, expected in not_raise_exception:
        assert grade(score) == expected
    for score, _ in raise_exception:
        with pytest.raises(Exception):
            grade(score)


# parametrize を使うとどのパラメータがテストに通らなかったか全部見ることができる
@pytest.mark.parametrize(('score', 'expected'), TEST_PARAMETERS)
def test_grade(score: int, expected: Union[str, Exception]):
    if isinstance(expected, str):
        assert grade(score) == expected
    else:
        with pytest.raises(Exception):
            grade(score)
