from app.main import parse

import pytest


@pytest.mark.parametrize(('code', 'expected'), [
    (100, 'Informational'),
    (199, 'Informational'),
    (200, 'Success'),
    (299, 'Success'),
    (300, 'Redirection'),
    (399, 'Redirection'),
    (400, 'ClientError'),
    (499, 'ClientError'),
    (500, 'ServerError'),
    (599, 'ServerError'),
])
def test_parse(code: int, expected: str):
    assert parse(code) == expected


@pytest.mark.parametrize('code', [
    99,
    600
])
def test_parse_irregular_code(code: int):
    with pytest.raises(Exception):
        parse(code)
