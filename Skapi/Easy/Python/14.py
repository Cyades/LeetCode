# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        temp = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(temp):
                temp = temp[:-1]
            if not temp:
                return ""
        return temp
