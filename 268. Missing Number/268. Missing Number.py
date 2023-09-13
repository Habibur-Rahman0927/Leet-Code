class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums) + 1
        # sum_ = int((n/2) * (n - 1))
        # return sum_ - sum(nums)

        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i 
        return len(nums)


solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))