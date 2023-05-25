class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])

        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum  = a + nums[l] + nums[r]
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
                if threeSum < target:
                    l += 1
                else:
                    r -= 1
        return res
    
solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))