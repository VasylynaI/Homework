import pytest

from homework10 import generate_random_integer, generate_random_string

rand_int = generate_random_integer()
rand_string = generate_random_string()


def test_generate_random_integer():
    assert -10 ** 10 <= rand_int <= 10 ** 10


def test_return_type_generate_random_integer():
    assert isinstance(rand_int, int)


def test_return_type_generate_random_string():
    assert isinstance(rand_string, str)


def test_len_generate_random_string():
    assert len(rand_string) == 10


def test_islower_generate_random_string():
    assert rand_string.islower()


def test_generate_random_string_expected_error():
    with pytest.raises(ValueError):
        generate_random_string(0)
