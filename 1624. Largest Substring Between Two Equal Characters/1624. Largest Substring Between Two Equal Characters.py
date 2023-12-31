class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        res = -1

        for i, c in enumerate(s):
            if c not in char_index:
                char_index[c] = i
            else: 
                res = max(res, i - char_index[c] - 1)
        return res

solution = Solution()
print(solution.maxLengthBetweenEqualCharacters("abca"))