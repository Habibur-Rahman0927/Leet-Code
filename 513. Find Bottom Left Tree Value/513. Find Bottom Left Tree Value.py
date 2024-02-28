# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(None)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

root.left.left.left = TreeNode(None)
root.left.left.right = TreeNode(None)

root.right.left.left = TreeNode(9)

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
    
        queue = [root]
        last_level_left_value = None
    
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == 0:
                    last_level_left_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return last_level_left_value
solution = Solution()
print(solution.findBottomLeftValue(root))