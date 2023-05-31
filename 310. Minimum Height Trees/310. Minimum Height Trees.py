import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        g = collections.defaultdict(set)
        for i, j in edges:
            g[i].add(j)
            g[j].add(i)

        print(g)
        q = [x for x in g if len(g[x]) == 1]
        print(q)

        while n > 2:
            n -= len(q)
            t = []
            for j in q:
                i = g[j].pop()
                g[i].remove(j)
                if len(g[i]) == 1:
                    t.append(i)
            q=t
        return q
    
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

solution = Solution()
print(solution.findMinHeightTrees(n, edges))