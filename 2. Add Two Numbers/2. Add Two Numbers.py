# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        result = ListNode(0)
        pointer = result
        
        
        while (l1 or l2 or carry):
            
            first_num = l1.val if l1 else 0
            second_num = l2.val if l2 else 0
            
            summation = first_num + second_num + carry
            
            num = summation % 10
            carry = summation // 10
            
            pointer.next = ListNode(num)
            
            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next
    
