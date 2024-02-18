class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        l = len(gain) + 1
        prefix_sum = [0] * l
        
        for i in range(1, l):
            prefix_sum[i] = prefix_sum[i - 1] + gain[i - 1]
        
        return max(prefix_sum)

solution = Solution()
print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))