class Solution(object):
    def guessNumber(self, n):
    
        if guess(n) == 0:
            return n
        left, right = 1,n
        while left < right:
            mid = int((left+right)/2)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid
            else:
                left = mid
                
