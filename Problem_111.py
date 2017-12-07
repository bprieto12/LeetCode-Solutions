"""
MINIMUM DEPTH OF BINARY TREE

Problem:
---------
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along 
the shortest path from the root node down to the nearest leaf node.

Idea:
-----
This sounds like level order traversal could solve this.  We should go down the
tree level by level until we reach the first node that is a leaf 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
def bfs(root, q, level):
        if root == None or q.empty():
            return 0
        if (root.left == None and root.right == None):
            return level

        if root.left != None:
            q.put(root.left)

        if root.right != None:
            q.put(root.right)

        child_root = q.get()
        return bfs(child_root, q, level + 1)
    
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
        q.put(root)
        level = 1

        return bfs(root, q, level)


