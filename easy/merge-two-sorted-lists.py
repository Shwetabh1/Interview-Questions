'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # when one of the lists is empty we simply return the other list
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
        
        # we need a placeholder node where we build our merged linked list
        placeholder = ListNode(0)
        head = placeholder
        
        while (l1 and l2):
            if l1.val <= l2.val:
                placeholder.next = l1
                l1 = l1.next
            else:
                placeholder.next = l2
                l2 = l2.next
            
            placeholder = placeholder.next
        
        if not l1:
            placeholder.next = l2
        else:
            placeholder.next = l1
        
        return head.next