"""
LINKED LIST CYCLE

Problem:
--------
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Works but it's slow O(N^2)
        fixed_node = head
        
        while fixed_node != None:
            back_pointer = head
            while back_pointer != fixed_node:
                if fixed_node.next == back_pointer:
                    return True
                back_pointer = back_pointer.next
            if fixed_node.next == back_pointer:
                return True
            fixed_node = fixed_node.next        
        return False



