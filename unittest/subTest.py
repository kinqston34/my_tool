import unittest
import sys

class NumbersTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("測試開始 ...")

    @classmethod
    def tearDownClass(cls):
        print("測試結束 ...")

    def test_odd(self):

        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i % 2 ,1)

    @unittest.skipIf(sys.version_info < (3 , 12),"以下測試只支援python 3.12以上")

    def test_even(self):

        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i % 2 ,0)

if __name__ == "__main__":
    print(sys.version_info < (3 , 12))
    unittest.main()