import unittest
import connection


class TestConnection(unittest.TestCase):

    def test_get_card_info(self):
        answer = connection.get_card_info(1893).card_id
        self.assertEqual(answer, 1893)
        answer = connection.get_card_info(9842).holder_name
        self.assertEqual(answer, 'Benito Testerini')


if __name__ == '__main__':
    unittest.main()
