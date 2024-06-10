class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res


solution = Solution()
print(solution.heightChecker([1,1,4,2,1,3]))