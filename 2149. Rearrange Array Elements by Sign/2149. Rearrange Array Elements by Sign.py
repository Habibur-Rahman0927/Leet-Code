class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive_number = []
        negitive_number = []
        result = []
        for num in nums:
            if num < 0:
                negitive_number.append(num)
            else:
                positive_number.append(num)
                
        for p_num, n_num in zip(positive_number, negitive_number):
            result.append(p_num)
            result.append(n_num)
        return result


solution = Solution()
print(solution.rearrangeArray([3,1,-2,-5,2,-4]))