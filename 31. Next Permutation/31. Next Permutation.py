class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        
        pointer = length - 2

        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        
        if pointer == -1:
            return nums.reverse()
        
        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break
        nums[pointer + 1:] = reversed(nums[pointer + 1:])
        

solution = Solution()
print(solution.nextPermutation([1,2,3]))