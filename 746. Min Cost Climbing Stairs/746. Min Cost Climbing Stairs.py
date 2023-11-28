class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        return min(cost[-2],cost[-1])

solution = Solution()
print(solution.minCostClimbingStairs([10,15,20]))