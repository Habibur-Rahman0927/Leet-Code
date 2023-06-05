# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []

        def tervers(root, path):
            if not root:
               return []
            if not root.left and not root.right:
                return result.append(path+str(root.val))
            if root.left:
                tervers(root.left, path+str(root.val)+"->")
            if root.right:
                tervers(root.right, path+str(root.val)+"->")
        tervers(root, "")
        return result

root = TreeNode(1)         # root node
root.left = TreeNode(2)    # left child node
root.right = TreeNode(3)   # right child node
root.left.left = TreeNode(4)   # left child of left child node
root.left.right = TreeNode(5)

solution = Solution()
print(solution.binaryTreePaths(root))