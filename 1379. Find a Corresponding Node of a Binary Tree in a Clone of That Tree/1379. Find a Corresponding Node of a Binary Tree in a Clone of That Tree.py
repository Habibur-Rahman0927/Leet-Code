# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if not original:
            return None
        stack = collections.deque([(original, cloned)])
        while stack:
            og, clone = stack.popleft()
            if og == target:
                return clone
            if og.left:
                stack.append((og.left, clone.left))
            if og.right:
                stack.append((og.right, clone.right))
        