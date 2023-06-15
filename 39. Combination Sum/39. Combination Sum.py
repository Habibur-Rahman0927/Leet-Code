from collections import deque
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append((target, [], 0))
        ans = []
        while queue:
            cur_target, cur_ans, cand_idx = queue.popleft()
            for i in range(cand_idx, len(candidates)):
                new_target = cur_target - candidates[i]
                if new_target == 0:
                    ans.append(cur_ans + [candidates[i]])
                elif new_target > 0:
                    queue.append((cur_target - candidates[i], cur_ans + [candidates[i]], i))
        return ans

candidates = [2,3,6,7]
target = 7
solution = Solution()
print(solution.combinationSum(candidates, target))