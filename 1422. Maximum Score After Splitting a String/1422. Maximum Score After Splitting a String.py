class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = 0
        one = s.count('1')
        res = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, one + zero)
        return res


solution = Solution()
print(solution.maxScore("011101"))