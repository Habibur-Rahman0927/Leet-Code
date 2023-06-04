import collections
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        indegrees = collections.defaultdict(int)
        for u,v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
        for node in indegrees:
            if indegrees[node] == len(edges): return node


solution = Solution()
# print(solution.findCenter([[1,2],[2,3],[4,2]]))
print(solution.findCenter([[1,2],[5,1],[1,3],[1,4]]))