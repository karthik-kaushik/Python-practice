

class Solution:
    def canCompleteCircuit(self, gas, cost):
        tank=[]
        n=len(gas)
        for g,c in zip(gas,cost):
            tank.append(g-c)
        if sum(tank)<0:
            return -1
        flag=0
        start=0
        for i in range(len(tank)):
            flag+=tank[i]
            if flag<0:
                start=i+1
                flag=0
        return start

tc=Solution()
print(tc.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))