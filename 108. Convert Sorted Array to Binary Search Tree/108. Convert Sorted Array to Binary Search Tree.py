# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0: return None 
            
        if len(nums) == 1: return TreeNode(nums[0])

        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node