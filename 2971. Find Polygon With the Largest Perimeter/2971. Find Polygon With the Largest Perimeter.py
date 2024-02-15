class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = -1
        total = 0
        for n in nums:
            if total > n:
                res = total + n
            total += n
        return res
solution = Solution()
solution.largestPerimeter([1,12,1,2,5,50,3])