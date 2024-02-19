class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            total_sum -= num
            if left_sum == total_sum:
                return i
            left_sum += num
        return -1