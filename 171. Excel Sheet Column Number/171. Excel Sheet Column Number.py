class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        s = columnTitle.upper()
        number = 0

        for ch in s:
            number = number * 26
            number += ord(ch) - ord('A') + 1

        return number
    
solution = Solution()
print(solution.titleToNumber('A'))