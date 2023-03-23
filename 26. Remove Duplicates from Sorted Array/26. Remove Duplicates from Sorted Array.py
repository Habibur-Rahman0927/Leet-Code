class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # k = 0
        # for i in range(len(nums)):
        #     if i < len(nums) - 1 and nums[i] == nums[i+1]:
        #         continue
        #     nums[k] = nums[i]
        #     k += 1
        # return k
        
        if len(nums)<2:
            return len(nums)
        
        pre = 0
        for cur in range(1,len(nums)):
            if nums[cur]!=nums[pre]:
                pre+=1
                nums[pre]=nums[cur]

        return pre+1



solution = Solution()
print(solution.removeDuplicates([1,1,2,2]))