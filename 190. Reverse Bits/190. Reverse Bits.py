class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
    

solution = Solution()
print(solution.reverseBits(11111111111111111111111111111101))