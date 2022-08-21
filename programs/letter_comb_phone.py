from itertools import product
import string
class Solution:
    def letterCombinations(self,digits):
        table={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]}
        out=table[int(digits[0])]
        for digit in digits[1:]:
            insi =table[int(digit)]
            temp=[]
            for v1,v2 in product(insi,out):
                temp.append(v2+v1)
            out=temp
            out.sort()
        return out




   