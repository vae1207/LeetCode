class Solution(object):
    def findTheDifference(self, s, t):

        list_s = list(s)
        list_t = list(t)
        
        for i in range(len(list_s)):
            for j in range(len(list_t)):
                if list_s[i] == list_t[j]:
                    del list_t[j]
                    break
                    
        result = "".join(list_t)
        
        return result
