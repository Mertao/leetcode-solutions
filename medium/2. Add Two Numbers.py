#  Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        res_1 = str(l1.val)
        res_2 = str(l2.val)

        res_1_obj = l1.next
        res_2_obj = l2.next

        while res_1_obj:
            res_1 += str(res_1_obj.val)
            res_1_obj = res_1_obj.next

        while res_2_obj:
            res_2 += str(res_2_obj.val)
            res_2_obj = res_2_obj.next

        # переворачиваем строки и складываем получившиеся числа
        for x in str(int(res_1[::-1]) + int(res_2[::-1])):
            result.append(ListNode(x))

        # определяем next в нашем списке
        for x in range(len(result)-1, 0, -1):
            result[x].next = result[x-1]

        return result[-1]
