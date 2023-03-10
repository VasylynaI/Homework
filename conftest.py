import pytest

from homework12 import Mobile, Laptop


@pytest.fixture(scope='class')
def mobile():
    mobile_data = Mobile(
        brand='Apple',
        modal='XR',
        ram=128,

    )
    yield mobile_data


@pytest.fixture(scope='class')
def laptop():
    laptop_data = Laptop(
        brand='Lenovo',
        modal='XP',
        ram=64,
    )
    yield laptop_data
