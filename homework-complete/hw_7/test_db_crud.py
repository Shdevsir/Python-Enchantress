import unittest
from db_crud import CRUDu, CRUDc
import random
import string


class TestBaseConnection(unittest.TestCase):
    def setUp(self) -> None:
        letters = string.ascii_lowercase
        rund_name = ''.join(random.choice(letters) for i in range(10))
        fake_rund_name = ''.join(random.choice(letters) for i in range(10))
        self.dbt = CRUDu()
        self.dbtc = CRUDc()
        self.user_info = {
            'name': rund_name,
            'email': 'shdevsir@gmail.com',
            'registration_time': '2020-01-01 11:45:00'
        }
        self.fake_user_info = {
            'name': fake_rund_name,
            'email': 'fake_shdevsir@gmail.com',
            'registration_time': '2020-01-01 11:46:00'
        }
        self.cart = {
            'creation_time': '2020-03-08 16:00:00',
            'user_id': 2,
            'cart_details': [{'cart_id': 5, 'price': 200, 'product': 'apple'}]
        }
        self.cart_upd = {
            'creation_time': '2020-03-08 16:00:00',
            'user_id': 3,
            'cart_details': [{'cart_id': 5, 'price': 300, 'product': 'knife'}]
        }

        self.info_dict_r = [(10, 5, 200, 'apple'),
                            (11, 5, 200, 'apple')]
        self.info_dict_u = [(12, 5, 300, 'knife'),
                            (13, 5, 300, 'knife')]

    def test_CRUDu(self):
        self.dbt.create_user(self.user_info)
        last_id = self.dbt.last_user_id()
        read_info = self.dbt.read_user(last_id)
        self.assertEqual(read_info[0], self.user_info['name'])
        self.assertNotEqual(read_info[0], self.fake_user_info['name'])
        self.dbt.update_user(self.fake_user_info, 4)
        self.assertNotEqual(read_info[0], self.fake_user_info['name'])
        self.dbt.delete_user(last_id)
        self.assertNotEqual(read_info[0], self.fake_user_info['name'])

    def test_CRUDc(self):
        self.dbtc.create_cart(self.cart)
        read_info = self.dbtc.read_cart(5)
        self.assertEqual(read_info[0], self.info_dict_r[0])
        self.dbtc.create_cart(self.cart_upd)
        self.dbtc.update_cart(self.cart)
        self.assertEqual(read_info[0], self.info_dict_r[0])
        self.dbtc.delete_cart(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
