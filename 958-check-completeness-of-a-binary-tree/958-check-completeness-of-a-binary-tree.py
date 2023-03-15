import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: 
            return True
        res = []
        q = collections.deque([(root, 1)])
        while q:
            root, pos = q.popleft()
            res.append(pos)
            if root.left:
                q.append((root.left, 2 * pos))
            if root.right:
                q.append((root.right, 2 * pos + 1))
        return len(res) == res[-1]