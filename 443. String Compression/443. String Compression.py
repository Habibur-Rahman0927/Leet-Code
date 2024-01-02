class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # char_hasMap = {}
        # for c in chars:
        #     if c in char_hasMap:
        #         char_hasMap[c] += 1
        #     else:
        #         char_hasMap[c] = 1

        # total_count = 0
        # result = []
        # for char, count in char_hasMap.items():
        #     result.extend(list(str(char)))
        #     if count < 10:
        #         total_count += int(count)
        #     if count > 1:
        #         if count < 10:
        #             result.extend(list(str(count)))
        #         else:
        #             result.extend(list(str(count)))
        #             total_count += sum(int(s) for s in list(str(count)))
        
        # return result

        i = 0
        count = 1
        for j in range(1, len(chars) + 1):
            if j < len(chars) and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i += 1
                count = 1
        return i


solution = Solution()
print(solution.compress(["a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))