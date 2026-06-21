# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            s = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    s = False
                    break
            if s:
                return  i
        return -1