import collections
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, n = 0, len(nums)
        dp = [collections.defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]
        return res

solution = Solution()
print(solution.numberOfArithmeticSlices([2,4,6,8,10]))