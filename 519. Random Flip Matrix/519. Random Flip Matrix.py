class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.M = m
        self.N = n
        self.total = self.M * self.N
        self.fliped = set()

    def flip(self):
        """
        :rtype: List[int]
        """
        pos = random.randint(0, self.total - 1)
        while pos in self.fliped:
            pos = random.randint(0, self.total - 1)
        self.fliped.add(pos)
        return [pos / self.N, pos % self.N]

    def reset(self):
        """
        :rtype: void
        """
        self.fliped.clear()

solution = Solution(["Solution", "flip", "flip", "flip", "reset", "flip"], [[3, 1], [], [], [], [], []])
print(solution.flip())
print(solution.reset())