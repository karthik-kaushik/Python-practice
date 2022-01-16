import unittest

class Solution:




def regular_test():
    Test=[1,1]
    assert Solution().maxArea(Test)==1,"""should be """

def edge_test():
    Test=[1,8,6,2,5,4,8,3,7]
    assert Solution().maxArea(Test)==49,"""should be """


if __name__ == "__main__":
    regular_test()
    edge_test()
    print("pass")