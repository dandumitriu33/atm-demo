import unittest
import utils


class TestUtils(unittest.TestCase):

    def test_validate_withdraw_amount(self):
        answer = utils.validate_withdraw_amount(400)
        self.assertEqual(answer, True)
        answer = utils.validate_withdraw_amount(410)
        self.assertEqual(answer, False)
        answer = utils.validate_withdraw_amount(0)
        self.assertEqual(answer, False)
        answer = utils.validate_withdraw_amount(201)
        self.assertEqual(answer, False)
        answer = utils.validate_withdraw_amount(300.5)
        self.assertEqual(answer, False)


if __name__ == '__main__':
    unittest.main()
