
import sys
sys.path.append('../Python-practice')


from programs.container_with_water import Solution
def test_Regular():
    Test=[1,1]
    assert Solution().maxArea(Test)==1,"should be 1"

def test_edge():
    Test=[1,8,6,2,5,4,8,3,7]
    assert Solution().maxArea(Test)==49,"should be 49"

