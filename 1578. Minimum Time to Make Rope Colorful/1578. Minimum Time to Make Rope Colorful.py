class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        res = 0
        maxNeededTime = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
               res += min(maxNeededTime, neededTime[i])
               maxNeededTime = max(maxNeededTime, neededTime[i])
            else:
                maxNeededTime = neededTime[i]
        return res


solution = Solution()
solution.minCost(colors = "aabaa", neededTime = [1,2,3,4,1])