# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = None
        self.ans = float("inf")

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.val is not None:
                self.ans = min(self.ans, abs(root.val - self.val))
            self.val = root.val
            inorder(root.right)

        inorder(root)
        return self.ans
    

root = TreeNode(1)         # root node
root.left = TreeNode(2)    # left child node
root.right = TreeNode(3)   # right child node
root.left.left = TreeNode(4)   # left child of left child node
root.left.right = TreeNode(5)

solution = Solution()
print(solution.getMinimumDifference(root))