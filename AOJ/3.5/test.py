import unittest
from alds1_2_c import cardnum, cardlabel

class MyTestCase(unittest.TestCase):
    def test_cardnum_1(self):
        card = "H1"
        self.assertEqual(cardnum(card),1)

    def test_cardlabel(self):
        card = "H1"
        self.assertEqual(cardlabel(card),"H")

if __name__ == '__main__':
    unittest.main()
