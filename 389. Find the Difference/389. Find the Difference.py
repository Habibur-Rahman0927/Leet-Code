from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = Counter(t)
        for tl in s:
            if tl in count:
                count[tl] -= 1

        for key, value in count.items():
            if value == 1:
                return key
        return None
        

solution = Solution()
print(solution.findTheDifference("a", "aa"))