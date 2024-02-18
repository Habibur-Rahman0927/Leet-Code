import heapq
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        return count.index(max(count))

solution = Solution()
print(solution.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))