class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)
        return res + 1 if seen else res