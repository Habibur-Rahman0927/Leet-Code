from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        adjacency_matrix = defaultdict(list)
        quaue = [root]

        while quaue:
            node = quaue.pop(0)
            if node.left:
                quaue.append(node.left)
                adjacency_matrix[node.val].append(node.left.val)
                adjacency_matrix[node.left.val].append(node.val)

            if node.right:
                quaue.append(node.right)
                adjacency_matrix[node.val].append(node.right.val)
                adjacency_matrix[node.right.val].append(node.val)
        
        quaue = [(start, 0)]
        visited = set()
        visited.add(start)

        while quaue:
            node, time = quaue.pop(0)

            for neighbour in adjacency_matrix[node]:
                if neighbour not in visited:
                    quaue.append((neighbour, time + 1))
                    visited.add(neighbour)
        return time