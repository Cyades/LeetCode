# https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        total = 0
        list = [a for a in s]
        for i in range (len(list)):
            curr_val = dict[list[i]]
            if i + 1 < len(list) and curr_val < dict[s[i+1]]:
                total -= curr_val
            else:
                total += curr_val
        return total