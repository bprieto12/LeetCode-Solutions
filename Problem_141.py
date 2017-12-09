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
        node_cache = {}

        moving_head = head
        while moving_head != None:
            if moving_head in node_cache:
                return True
            else:
                node_cache[moving_head] = 1
            moving_head = moving_head.next
        return False


