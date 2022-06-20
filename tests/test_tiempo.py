import unittest
import eltiempo



class MyTestCase(unittest.TestCase):
    def test_printResult(self):
        self.assertEqual(eltiempo.printResult("máximo","25"),
                         "Temperatura máximo : 25")


if __name__ == '__main__':
    unittest.main()
