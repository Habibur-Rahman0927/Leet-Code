class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # i = 0
        # while i < len(nums) - 2:
        #     if nums[i] < nums[i + 1] and nums[i + 1] < nums[i + 2]:
        #         return True
        #     i += 1
        # return False
        # count = 0
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] < nums[i + 1]:
        #         count += 1
        #         if count == 3:
        #             return True
        # return False

        min1 = float('inf')
        min2 = float('inf') 

        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True

        return False


solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))
