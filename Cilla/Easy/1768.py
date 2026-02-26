# 1768. merge strings alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        
        w1 = len(word1)
        w2 = len(word2)

        for i in range(max(w1, w2)):
            if i < w1:
                result += word1[i]
            if i < w2:
                result += word2[i]
        return result