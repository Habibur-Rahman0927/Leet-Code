from collections import Counter, defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        buckets = defaultdict(list)

        for char, cnt in count.items():
            buckets[cnt].append(char)
        
        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        return "".join(res)

solution = Solution()
print(solution.frequencySort("raaeaedere"))