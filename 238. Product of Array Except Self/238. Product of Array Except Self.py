from functools import reduce
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # i = 0
        # while i < len(nums):
        #     multiplication = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             multiplication *= nums[j]
        #     result.append(multiplication)
        #     i += 1
        # return result

        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        result = [0] * n
    
        for i in range(1, n):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        
        for i in range(n):
            result[i] = prefix_product[i] * suffix_product[i]
    
        return result

    
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))