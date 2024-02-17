import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heights) - 1

solution = Solution()
print(solution.furthestBuilding([4,2,7,6,9,14,12], 5, 1))