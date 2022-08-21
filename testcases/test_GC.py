
import sys
sys.path.append('../Python-practice')


from programs.gas_station import Solution
def test_Regular():
    assert Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])==3,"should be 3"
    


