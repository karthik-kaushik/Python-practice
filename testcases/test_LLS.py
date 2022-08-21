
import sys
sys.path.append('../Python-practice')


from programs.linked_list_sum import Solution,ListNode

def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head

def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def test_1():
    assert to_native_list(Solution().addTwoNumbers(to_linked_list([2,4,3]),to_linked_list([5,6,4])))==[7,0,8],"""[7,0,8] is expected"""

def test_2():
    assert to_native_list(Solution().addTwoNumbers(to_linked_list([0]),to_linked_list([0])))==[0],"""[0] is expected"""

def test_3():
    assert to_native_list(Solution().addTwoNumbers(to_linked_list([9,9,9,9,9,9,9]),to_linked_list([9,9,9,9])))==[8,9,9,9,0,0,0,1],"""[8,9,9,9,0,0,0,1] is expected"""

[7,0,8]
[0]
[8,9,9,9,0,0,0,1]