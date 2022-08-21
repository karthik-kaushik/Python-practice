
import unittest

class Solution:
    def maxArea(self, height):
        start=0
        end=len(height)-1
        out=0
        while start<end:
            a=height[start]
            b=height[end]
            if a<b:
                flag=1
                leng=a
            else:
                flag=0
                leng=b
            area=leng*(end-start)
            if out<area:
                out=area
            if flag:
                start+=1
            else:
                end-=1
        
        return out;


def regular_test():
    Test=[1,1]
    assert Solution().maxArea(Test)==1,"should be 1"

def edge_test():
    Test=[1,8,6,2,5,4,8,3,7]
    assert Solution().maxArea(Test)==49,"should be 49"

