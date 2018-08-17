import unittest
import newslettersms


class Testmain(unittest.TestCase):

    def test_def_vars(self):
        vals, vals_api = newslettersms.def_vars('../.conf', '../.env')

        self.assertEqual(vals['time'], 745)

    def test_news_api(self):
        vals, vals_api = newslettersms.def_vars('../.conf', '../.env')

        arraye = ['94074cd9596f4e2a812c7e6eb286ac7f', 1, 5]

        self.assertEqual(vals_api['news'], arraye)

if __name__ == '__main__':
    unittest.main()
