
import sys
sys.path.append('../Python-practice')


from programs.letter_comb_phone import Solution

def test_regular_test():
    digits = "23"
    assert Solution().letterCombinations(digits)==["ad","ae","af","bd","be","bf","cd","ce","cf"],"""should be ["ad","ae","af","bd","be","bf","cd","ce","cf"]"""

def test_edge_test():
    digits = "2"
    assert Solution().letterCombinations(digits)==["a","b","c"],"""should be ["a","b","c"]"""
