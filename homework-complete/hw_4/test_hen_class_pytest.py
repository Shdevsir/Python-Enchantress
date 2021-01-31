from hw_4 import hen_class as hen
import pytest
from unittest.mock import patch


def test_init_with_less_than_min():
    with pytest.raises(ValueError):
        hen.HenHouse(1)


@pytest.mark.parametrize(
    "hen_class, season, month",
    (
            (hen.HenHouse(10), 'winter', 1),
            (hen.HenHouse(5), 'spring', 3),
            (hen.HenHouse(11), 'summer', 6),
            (hen.HenHouse(20), 'autumn', 9),
    ),
)
def test_season(hen_class, season, month):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = month
        assert hen_class.season == season


@pytest.mark.parametrize(
    "hen_class, seasons, index",
    (
            (hen.HenHouse(10), 1, 0.25),
            (hen.HenHouse(20), 3, 0.75),
            (hen.HenHouse(5), 6, 1),
            (hen.HenHouse(11), 9, 0.5),
    ),
)
def test_productivity_index(hen_class, index, seasons):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = seasons
        assert hen_class._productivity_index() == index


@pytest.mark.parametrize(
    "hen_class, seasons",
    (
            (hen.HenHouse(10), 13),
            (hen.HenHouse(20), 30),
            (hen.HenHouse(5), 60),
            (hen.HenHouse(11), 90),
    ),
)
def test_productivity_index_incorrect_season(hen_class, seasons):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = seasons
        with pytest.raises(hen.ErrorTimesOfYear):
            hen_class._productivity_index()


@pytest.mark.parametrize(
    "hen_class, seasons, index",
    (
            (hen.HenHouse(10), 1, 1),
            (hen.HenHouse(20), 3, 4),
            (hen.HenHouse(5), 6, 6),
            (hen.HenHouse(11), 9, 3),
    ),
)
def test_get_eggs_daily_in_winter(hen_class, seasons, index):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = seasons
        assert hen_class.get_eggs_daily(6) == index


@pytest.mark.parametrize(
    "hen_class, seasons, index",
    (
            (hen.HenHouse(10), 1, 0),
            (hen.HenHouse(20), 3, 13),
            (hen.HenHouse(5), 6, 0),
            (hen.HenHouse(15), 9, 4),
    ),
)
def test_get_max_count_for_soup(hen_class, seasons, index):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = seasons
        assert hen_class.get_max_count_for_soup(5) == index


@pytest.mark.parametrize(
    "hen_class, seasons",
    (
            (hen.HenHouse(10), 10),
            (hen.HenHouse(20), 3),
            (hen.HenHouse(5), 6),
            (hen.HenHouse(15), 9),
    ),
)
def test_get_max_count_for_soup_returns_zero(hen_class, seasons):
    with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
        mock_obj.today().month = seasons
        assert hen_class.get_max_count_for_soup(100) == 0


@pytest.mark.parametrize(
    "hen_class, index",
    (
            (hen.HenHouse(10), 9),
            (hen.HenHouse(20), 9),
            (hen.HenHouse(5), 9),
            (hen.HenHouse(15), 9),
    ),
)
def test_food_price(hen_class, index):
    with patch('hw_4.hen_class.requests.get') as response:
        response.return_value.status_code = 200
        response.return_value.text = '12345678919'
        assert hen_class.food_price() == index


@pytest.mark.parametrize(
    "hen_class, index",
    (
            (hen.HenHouse(10), 100),
            (hen.HenHouse(20), 404),
            (hen.HenHouse(5), 300),
            (hen.HenHouse(15), -100),
    ),
)
def test_food_price_connection_error(hen_class, index):
    with patch('hw_4.hen_class.requests.get') as response:
        response.return_value.status_code = index
        with pytest.raises(ConnectionError):
            hen_class.food_price()