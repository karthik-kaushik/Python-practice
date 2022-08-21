import unittest

class Solution:
    def letterCombinations(self, digits):
        table={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]}
            



def regular_test():
    digits = "23"
    assert Solution().letterCombinations(digits)==["ad","ae","af","bd","be","bf","cd","ce","cf"],"""should be ["ad","ae","af","bd","be","bf","cd","ce","cf"]"""

def edge_test():
    digits = "2"
    assert Solution().letterCombinations(digits)==["a","b","c"],"""should be ["a","b","c"]"""


if __name__ == "__main__":
    regular_test()
    edge_test()
    print("pass")


   