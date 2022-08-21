
import sys
import unittest
# setting path
sys.path.append('../Python-practice')
from programs.container_with_water import Solution


    

class TestingApp(unittest.TestCase):

    def test_Regular(self):
        Test=[1,1]
        self.assertTrue(Solution().maxArea(Test)==1,"should be 1")

    def test_edge(self):
        Test=[1,8,6,2,5,4,8,3,7]
        self.assertTrue(Solution().maxArea(Test)==49,"should be 49")


if __name__ == "__main__":
    unittest.main()