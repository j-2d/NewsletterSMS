import unittest
import newslettersms


class Testmain(unittest.TestCase):

    def test_def_vars(self):
        vals, vals_api = newslettersms.def_vars('../.conf', '../.env')

        self.assertEqual(vals['time'], 745)

    def test_news_api(self):
        vals, vals_api = newslettersms.def_vars('../.conf', '../.env')

        self.assertEqual(vals_api['news'][1], 1)
        self.assertEqual(vals_api['news'][2], 5)

if __name__ == '__main__':
    unittest.main()
