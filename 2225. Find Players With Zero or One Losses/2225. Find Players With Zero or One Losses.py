from collections import Counter
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losses = Counter()
        for winner, loser in matches:
            losses[winner] += 0
            losses[loser] += 1

        ans = [[], []]
        for player in sorted(losses.keys()):
            if losses[player] == 0:
                ans[0].append(player)
            elif losses[player] == 1:
                ans[1].append(player)
        return ans

solution = Solution()
print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))