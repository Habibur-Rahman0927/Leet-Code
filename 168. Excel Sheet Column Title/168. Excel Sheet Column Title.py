class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        return self.convertToTitle((columnNumber - 1) // 26) + \
        chr(ord('A') + (columnNumber - 1) % 26) if columnNumber else ''
    
solution = Solution()
print(solution.convertToTitle(1))