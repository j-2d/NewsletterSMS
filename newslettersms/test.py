import unittest
import main


class Testmain(unittest.TestCase):

    def test_def_vars(self):
        main.def_vars('../conf', '../.env')


if __name__ == '__main__':
    unittest.main()
