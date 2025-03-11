#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_1.question_a import test_config, get_bonus_pay_amount

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


