import unittest
from unittest.mock import patch
from hw_3 import simple_employee as emp


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = emp.Employee('Jhon', 'Doi', 2000)

    def test_email(self):
        self.assertEqual(self.employee.email, 'Jhon.Doi@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Jhon Doi')

    def test_raise(self):
        number = self.employee.pay
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, int(number * self.employee.raise_amt))

    def test_good_response(self):
        with patch('hw_3.simple_employee.requests.get') as response:
            response.return_value.ok = True
            response.return_value.text = 'URL'
            schedule = self.employee.monthly_schedule(month=None)
            self.assertEqual(schedule, 'URL')

    def test_bad_response(self):
        with patch('hw_3.simple_employee.requests.get') as response:
            response.return_value.ok = False
            schedule = self.employee.monthly_schedule(month=None)
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main(verbosity=1)
