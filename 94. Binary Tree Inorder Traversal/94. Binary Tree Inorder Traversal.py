# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def traverse(root):
            if not root:
                return None
            if root.left is not None:
                traverse(root.left)
            result.append(root.val)
            if root.right is not None:
                traverse(root.right)
        traverse(root)
        return result
    

