class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        intervals = sorted(zip(startTime, endTime, profit))

        cache = {}

        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)

            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
        