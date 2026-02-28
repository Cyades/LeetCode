# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i+1]]:
                result += vals[s[i+1]] - vals[s[i]]
                i += 1
            else:
                result += vals[s[i]]
            i += 1
        
        return result