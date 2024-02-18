class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # f = [0] + flowerbed + [0]

        # for i in range(1, len(f) - 1):
        #     if f[i - 1] == 0 and f[i] == 0 and f [i + 1] == 0:
        #         f[i] = 1
        #         n -= 1
        # return n <= 0

        i = 0
        cnt = 0
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and (i <= 0 or flowerbed[i - 1] == 0) and (i >= len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                cnt += 1
                i += 1
            i += 1
        return n <= cnt

solution = Solution()
solution.canPlaceFlowers([1,0,0,0,1], 1)

