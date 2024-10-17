from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.testCases = {
            1: (1, 1, 7, "ccaccbcc"),
            2: (7, 1, 0, "aabaa")
        }
        self.obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        a, b, c, output = self.testCases[1]
        result = self.obj.longestDiverseString(a, b, c)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        a, b, c, output = self.testCases[2]
        result = self.obj.longestDiverseString(a, b, c)
        self.assertIsInstance(result, str)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()