import pytest

from code import AND, OR, TRUE, FALSE, NOT, XOR
from code import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX
from code import ADD, INC, MUL, POW
from code import ISZERO
from code import make_number


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  FALSE),
    (TRUE,  FALSE, FALSE),
    (TRUE,  TRUE,  TRUE),
])
def test_and(left, right, expected):
    assert AND(left)(right) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  TRUE),
])
def test_or(left, right, expected):
    assert OR(left)(right) is expected


@pytest.mark.parametrize('given, expected', [
    (FALSE, TRUE),
    (TRUE, FALSE),
])
def test_not(given, expected):
    assert NOT(given) is expected


@pytest.mark.parametrize('left, right, expected', [
    (FALSE, FALSE, FALSE),
    (FALSE, TRUE,  TRUE),
    (TRUE,  FALSE, TRUE),
    (TRUE,  TRUE,  FALSE),
])
def test_xor(left, right, expected):
    assert XOR(left)(right) is expected


@pytest.mark.parametrize('given, expected', [
    (ONE,   1),
    (TWO,   2),
    (THREE, 3),
    (FOUR,  4),
    (FIVE,  5),
    (SIX,   6),
])
def test_numbers(given, expected):
    assert make_number(given) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE,   ONE,   1),
    (TWO,   ONE,   2),
    (ONE,   TWO,   1),
    (THREE, TWO,   9),
    (THREE, THREE, 27),
])
def test_pow(left, right, expected):
    assert make_number(POW(left)(right)) == expected


@pytest.mark.parametrize('given, expected', [
    (ZERO,  1),
    (ONE,   2),
    (TWO,   3),
    (THREE, 4),
])
def test_incr(given, expected):
    assert make_number(INC(given)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE, ONE,   2),
    (TWO, THREE, 5),
    (THREE, TWO, 5),
])
def test_add(left, right, expected):
    assert make_number(ADD(left)(right)) == expected


@pytest.mark.parametrize('left, right, expected', [
    (ONE, ONE,   1),
    (TWO, THREE, 6),
    (THREE, TWO, 6),
])
def test_mul(left, right, expected):
    assert make_number(MUL(left)(right)) == expected


@pytest.mark.parametrize('given, expected', [
    (ZERO, TRUE),
    (ONE,  FALSE),
    (TWO,  FALSE),
])
def test_iszero(given, expected):
    assert ISZERO(given) is expected


if __name__ == '__main__':
    pytest.main()
