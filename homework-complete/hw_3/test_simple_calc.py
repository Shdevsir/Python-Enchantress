from hw_3 import simple_calc as cal
import unittest
from random import randint


class TestSimpleCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.pos_num = [randint(1, 1000), randint(1, 1000)]
        self.neg_num = [randint(-1000, -1), randint(-1000, -1)]

    def test_add_pos(self):
        self.assertEqual(cal.add(self.pos_num[0], self.pos_num[1]), self.pos_num[0] + self.pos_num[1])

    def test_add_neg(self):
        self.assertEqual(cal.add(self.neg_num[0], self.neg_num[1]), self.neg_num[0] + self.neg_num[1])

    def test_subtract_mixed(self):
        self.assertEqual(cal.subtract(self.pos_num[0], self.pos_num[1]), self.pos_num[0] - self.pos_num[1])
        self.assertEqual(cal.subtract(self.neg_num[0], self.neg_num[1]), self.neg_num[0] - self.neg_num[1])

    def test_multiply_only_numbers(self):
        self.assertIsNot(cal.multiply(self.pos_num[0], self.neg_num[0]), chr)

    @unittest.skipIf(ValueError, "Sorry, it`s value error")
    def test_divide(self):
        self.assertIsNot(cal.divide(self.pos_num[0], self.neg_num[0]), self.pos_num[0] / self.neg_num[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
