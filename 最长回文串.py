class Solution(object):
    def longestPalindrome(self, s):
       
        if s is None:
            return 0
        len_s = len(s)
        flag = 1
        for ch in set(s):
            if s.count(ch)%2!=0:
                len_s -= 1
                flag = 0
        if flag:
            return len(s)
        else:
            return len_s + 1
