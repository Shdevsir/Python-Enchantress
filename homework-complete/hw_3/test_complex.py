import unittest
from hw_3 import complex as com
from unittest import mock
from unittest.mock import MagicMock


class TestComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.complex = com.Test()

    def test_hello(self):
        self.assertEqual(self.complex.hello(), 1)

    @mock.patch('hw_3.complex.Test.__enter__', side_effect=MagicMock(return_value=1))
    def test_enter_with_mock(self, request):
        self.assertEqual(self.complex.__enter__(), 1)

    def test_new_test(self):
        self.assertIsInstance(com.new_test(), com.Test)

    def test_func(self):
        self.assertEqual(com.func(), 1)

    @mock.patch('hw_3.complex.Test.__exit__', side_effect=MagicMock(return_value=1))
    def test_exit(self, request):
        self.assertEqual(self.complex.__exit__(1, 1, 1), True)


if __name__ == '__main__':
    unittest.main(verbosity=1)
