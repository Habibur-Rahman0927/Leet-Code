class Solution:
  def numberOfArithmeticSlices(self, nums):
    n = len(nums)
    if n < 3:
      return 0

    dp = [0] * n

    for i in range(2, len(nums)):
      if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
        dp[i] = dp[i - 1] + 1

    return sum(dp)

solution = Solution()
print(solution.numberOfArithmeticSlices([1,2,3,4]))