class Solution(object):
    def titleToNumber(self, s):
        
        n = 0
        for ch in s:
            n = n*26 + ord(ch) - 65 + 1
        return n
