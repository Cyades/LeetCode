class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        list = [int(a) for a in str(x)]
        for i in range (len(list)):
            if list[i] != list[-(i + 1)]:
                print(list[i])
                print(list[-(i+1)])
                return False
    
        return True