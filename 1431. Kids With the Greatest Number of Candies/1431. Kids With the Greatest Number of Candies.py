class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = [True] * len(candies)
        max_number = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies < max_number:
                result[i] = False
        return result
        
solution = Solution()
print(solution.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))