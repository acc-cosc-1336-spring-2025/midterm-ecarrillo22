import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_1.question_a import test_config, get_bonus_pay_amount
from src.question_2.question_b import use_global
from src.question_3.question_c import get_random_number
from src.question_4.question_d import is_prime

global_variable = 50

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000),70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid arguments")

    def test_use_global(self):
        global global_variable
        print(global_variable)
        global_variable = use_global()
        print(global_variable)

    def test_get_random_number(self):
        self.assertEqual(get_random_number() >= 1, True)
        self.assertEqual(get_random_number() <= 5, True)

    def test_is_prime(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)