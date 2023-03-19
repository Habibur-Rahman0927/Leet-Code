import collections
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        neighbors = collections.defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in neighbors[node]:
                if dfs(n, end, seen):
                    return True
                
            return False
        
        seen = set()    
        return dfs(source, destination, seen)










