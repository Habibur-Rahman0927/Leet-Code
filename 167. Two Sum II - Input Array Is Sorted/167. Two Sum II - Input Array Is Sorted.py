class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l <= r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum == target:
                return [l+1,r+1]
            else:
                l += 1
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))