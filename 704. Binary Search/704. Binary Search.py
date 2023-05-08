class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == target: return i
        return -1


solution = Solution()
print(solution.search([-1,0,3,5,9,12], 9))