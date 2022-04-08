from container_with_water import Solution

def regular_test():
    Test=[1,1]
    assert Solution().maxArea(Test)==1,"should be 1"

def edge_test():
    Test=[1,8,6,2,5,4,8,3,7]
    assert Solution().maxArea(Test)==49,"should be 49"


if __name__ == "__main__":
    regular_test()
    edge_test()
    print("pass")