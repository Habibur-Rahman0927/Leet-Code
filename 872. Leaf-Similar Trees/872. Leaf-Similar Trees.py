# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        leaf1, leaf2 = [], []

        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2