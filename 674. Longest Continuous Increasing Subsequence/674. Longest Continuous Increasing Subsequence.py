class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = 0
        # achor = 0
        # for i in range(len(nums)):
        #     if i > 0 and nums[i - 1] >= nums[i]:
        #         achor = i
        #     result = max(result, i - achor + 1)
        # return result

        maxLen = count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count = 1
                
            maxLen = max(count, maxLen)
                
        return maxLen

solution = Solution()
print(solution.findLengthOfLCIS([1,3,5,4,7]))