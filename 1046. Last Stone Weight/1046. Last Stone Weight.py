import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        # print(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first: heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

solution = Solution()
print(solution.lastStoneWeight([2,7,4,1,8,1]))