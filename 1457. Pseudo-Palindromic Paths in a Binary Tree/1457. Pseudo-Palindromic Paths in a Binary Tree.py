# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root, 0)
def dfs(node,path):
    if not node:
        return 0
    counter = 0
    path = path ^ (1 << node.val)
    
    counter+=dfs(node.left, path)
    counter+=dfs(node.right, path)
    if not node.left and not node.right:
        if path & (path - 1) == 0:
            counter += 1
    return counter      