from collections import defaultdict
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        lk = defaultdict(int)
        i = 0
        for c in order:
            lk[c] = i
            i += 1
        return "".join(sorted(s, key=lambda x : lk[x]))
solution = Solution()
print(solution.customSortString("bcafg", "abcd"))