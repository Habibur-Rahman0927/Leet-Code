class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

        # result = [w1 + w2 for w1, w2 in zip(word1, word2)]
        # result.extend(word1[len(result):] + word2[len(result):])
        # return ''.join(result)
