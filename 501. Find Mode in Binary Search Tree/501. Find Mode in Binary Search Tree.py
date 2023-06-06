# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        count = {}
        def checkDups(root):
            if root.val not in count:count[root.val] = 1
            else:count[root.val] += 1
            if not root.left and not root.right:return
            if root.left:checkDups(root.left)
            if root.right:checkDups(root.right)
        checkDups(root)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]
