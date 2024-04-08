from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        return res


solution = Solution()
print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))