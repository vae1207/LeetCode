class Solution(object):
    def isPowerOfThree(self, n):
       
        if n == 1:
            return True
        
        while n != 0:
            if n == 3:
                return True
            if n % 3 == 0:
                n = n/3
                
            else:
                return False
        return False
