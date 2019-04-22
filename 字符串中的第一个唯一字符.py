class Solution(object):
    def firstUniqChar(self, s):
    
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i+1:]:
                return i
        return -1




        s_list = list(set(s))
        s_list.sort(key = s.index)
        for value in s_list:
            if s.count(value) == 1:
                return s.index(value)
        return -1
