from collections import defaultdict, Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # count = defaultdict()
        # count = Counter(magazine)
        # for maga in magazine:
        #     if maga not in count:
        #         count[maga] = 1
        #     else:
        #         count[maga] += 1

        # for rensom in ransomNote:
        #     if count[rensom] == 0:
        #         del count[rensom]
        #     if rensom in count and count[rensom] > 0:
        #         count[rensom] -= 1
        #     else:
        #         return False
        # return True


        i = 0
        while i < len(ransomNote):
            if ransomNote.count(ransomNote[i]) <= magazine.count(ransomNote[i]):
                ransomNote = ransomNote.replace(ransomNote[i],"")
            else:
                return False
            
        return True

solution = Solution()
print(solution.canConstruct(ransomNote = "aa", magazine = "aa"))