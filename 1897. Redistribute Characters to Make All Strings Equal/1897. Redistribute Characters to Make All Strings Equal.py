import collections

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        chart_cnt = collections.defaultdict(int)

        for w in words:
            for c in w:
                chart_cnt[c] += 1
        
        for c in chart_cnt:
            if chart_cnt[c] % len(words):
                return False
        return True

solution = Solution()
solution.makeEqual(["abc","aabc", "bc"])