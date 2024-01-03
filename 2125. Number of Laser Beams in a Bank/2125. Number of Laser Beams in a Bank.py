class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev = bank[0].count("1")
        res = 0

        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                res += (prev * curr)
                prev = curr
        return res

solution = Solution()
print(solution.numberOfBeams(["011001","000000","010100","001000"]))