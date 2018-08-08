import unittest
import newslettersms


class Testmain(unittest.TestCase):

    def test_def_vars(self):
        vals = newslettersms.def_vars('../.conf', '../.env')

        self.assertEqual(vals['time'], 745)


if __name__ == '__main__':
    unittest.main()
