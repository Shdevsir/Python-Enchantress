import unittest
from unittest.mock import patch
from unittest import mock
from hw_4 import hen_class as hen


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.hen_house = hen.HenHouse(5)

    def test_init_with_less_than_min(self):
        with self.assertRaises(ValueError):
            hen.HenHouse(3)

    def test_season(self):
        with patch('hw_4.hen_class.datetime.datetime') as mock_obj:
            mock_obj.today().month = 1
            self.assertEqual('winter', self.hen_house.season)

    @mock.patch('hw_4.hen_class.HenHouse.season', 'winter')
    def test_productivity_index(self):
        self.assertEqual(self.hen_house._productivity_index(), 0.25)

    @mock.patch('hw_4.hen_class.HenHouse.season', 'error_season')
    def test_productivity_index_incorrect_season(self):
        with self.assertRaises(hen.ErrorTimesOfYear):
            self.hen_house._productivity_index()

    @mock.patch('hw_4.hen_class.HenHouse.season', 'summer')
    def test_get_eggs_daily_in_winter(self):
        self.assertEqual(self.hen_house.get_eggs_daily(6), 6)

    @mock.patch('hw_4.hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup(self):
        self.assertEqual(self.hen_house.get_max_count_for_soup(5), 0)

    @mock.patch('hw_4.hen_class.HenHouse.season', 'summer')
    def test_get_max_count_for_soup_returns_zero(self):
        self.assertEqual(self.hen_house.get_max_count_for_soup(10), 0)

    def test_food_price(self):
        with patch('hw_4.hen_class.requests.get') as response:
            response.return_value.status_code = 200
            response.return_value.text = '12345678919'
            self.assertEqual(self.hen_house.food_price(), 9)

    def test_food_price_connection_error(self):
        with patch('hw_4.hen_class.requests.get') as response:
            response.return_value.status_code = 100
            with self.assertRaises(ConnectionError):
                self.hen_house.food_price()


if __name__ == '__main__':
    unittest.main()
