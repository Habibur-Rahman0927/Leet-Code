# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1,2,2)
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        stack = []
        stack.append(root.right)
        stack.append(root.left)
        
        while(stack):
            leftNode = stack.pop()
            rightNode = stack.pop()
            
            if leftNode == None and rightNode == None:
                continue
                
            if leftNode == None or rightNode == None or (leftNode.val != rightNode.val):
                return False
            
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            
            stack.append(leftNode.right)
            stack.append(rightNode.left)
            
        return True
    

    # recursive way
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def is_mirror(left, right):
    #         if not left and not right: return True
    #         if not left or not right or (left.val != right.val): return False
    #         return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    #     return is_mirror(root, root)
    


solution = Solution()
print(solution.isSymmetric(root))


