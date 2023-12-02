class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vewols = 'aeiouAEIOU'
        convertIntoList = list(s)
        i = 0
        j = len(s) - 1

        while (i < j):
            if convertIntoList[i] not in vewols:
                i += 1
                continue
            if convertIntoList[j] not in vewols:
                j -= 1
                continue
            convertIntoList[i], convertIntoList[j] = convertIntoList[j], convertIntoList[i]
            i += 1
            j -= 1
        return ''.join(convertIntoList)
        