# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = 0

        def helper(curr, cur_min, cur_max):
            if not curr:
                return
            result = max(self.result, abs(cur_max - curr.val), abs(cur_min - curr.val))
            cur_min = min(cur_min, curr.val)
            cur_max = max(cur_max, curr.val)
            helper(curr.left, cur_min, cur_max)
            helper(curr.right, cur_min, cur_max)

        helper(root, root.val, root.val)
        return result