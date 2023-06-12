class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        res = []
        products.sort()

        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            
            res.append([])
            remain = r - l + 1
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
        return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
solution = Solution()
solution.suggestedProducts(products, searchWord)