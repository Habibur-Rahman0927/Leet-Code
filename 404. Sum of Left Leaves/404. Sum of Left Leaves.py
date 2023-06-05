# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tervers(root):
            if root == None:
                return 0
            add = 0
            if root.left and (root.left.left is None and root.left.right is None):
                add += root.left.val
            return add + tervers(root.left) + tervers(root.right) 
            
        return tervers(root)
    
root = TreeNode(1)         # root node
root.left = TreeNode(2)    # left child node
root.right = TreeNode(3)   # right child node
root.left.left = TreeNode(4)   # left child of left child node
root.left.right = TreeNode(5)

solution = Solution()
print(solution.sumOfLeftLeaves(root))