from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q, ans = [root], []
        while len(q):
            qlen, row = len(q), 0
            for i in range(qlen):
                curr = q.pop(0)
                row += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(float(row)/qlen)
        return ans

root = TreeNode(1)         # root node
root.left = TreeNode(2)    # left child node
root.right = TreeNode(3)   # right child node
root.left.left = TreeNode(4)   # left child of left child node
root.left.right = TreeNode(5)

solution = Solution()
print(solution.averageOfLevels(root))