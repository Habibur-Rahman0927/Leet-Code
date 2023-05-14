import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt_1 = {}
        for s in s1: cnt_1[s] = cnt_1.get(s, 0) + 1
        len_s1 = len(s1)

        for i in range(len(s2) - len_s1 + 1):
            sub_str = s2[i: i + len_s1]
            cnt_2 = collections.Counter(sub_str)
            if cnt_1 == cnt_2:
                return True
        
        return False
    
solution = Solution()
print(solution.checkInclusion('ab', 'eidbaooo'))