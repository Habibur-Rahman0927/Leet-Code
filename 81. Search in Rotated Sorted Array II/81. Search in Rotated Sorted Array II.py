class Solution:
  def search(self, nums, target):
    nums = list(set(nums))
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
        
    lp = 0
    rp = len(nums) - 1
    while lp <= rp:
        mp = lp + rp >> 1
        if nums[mp] == target:
            return True
        
        if (target < nums[0] and not target < nums[mp] < nums[0] or
                target >= nums[0] and nums[0] <= nums[mp] < target):
            lp = mp + 1
        else:
            rp = mp - 1
            
    return False

solution = Solution()
print(solution.search([2,5,6,0,0,1,2], 0))