import collections
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        result = 0
        for c in tc:
            result += max(tc[c] - sc[c], 0)
        return result

solution = Solution()
print(solution.minSteps(s = "leetcode", t = "practice"))