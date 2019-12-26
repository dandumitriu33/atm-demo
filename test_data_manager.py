import unittest
import data_manager


class TestDataManager(unittest.TestCase):

    def test_get_specific_card_holder_name(self):
        answer = data_manager.get_specific_card_holder_name(9842)
        self.assertEqual(answer, 'Benito Testerini')
        answer = data_manager.get_specific_card_holder_name(8931)
        self.assertEqual(answer, 'Alfredo Test')

    def test_get_specific_card_type(self):
        answer = data_manager.get_specific_card_type(9842)
        self.assertEqual(answer, 'MC')
        answer = data_manager.get_specific_card_type(8931)
        self.assertEqual(answer, 'MC')

    def test_get_specific_card_bank_name(self):
        answer = data_manager.get_specific_card_bank_name(9842)
        self.assertEqual(answer, 'Gold Bank')
        answer = data_manager.get_specific_card_bank_name(8931)
        self.assertEqual(answer, 'Gold Bank')

    def test_get_specific_card_account_number(self):
        answer = data_manager.get_specific_card_account_number(9842)
        self.assertEqual(answer, 'IBAN1930183277892001')
        answer = data_manager.get_specific_card_account_number(8931)
        self.assertEqual(answer, 'IBAN31008901000018901')


if __name__ == '__main__':
    unittest.main()
