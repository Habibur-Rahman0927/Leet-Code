class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i = 0
        while i < k:
            temp = nums.pop()
            nums.insert(0, temp)
            i += 1
