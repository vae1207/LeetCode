class Solution(object):
    def reverseVowels(self, s):
   
        p = 0
        s = list(s)
        q = len(s) - 1
        y = ['a','o','e','i','u','A','O','E','I','U']
        while p <= q:
            if s[p] not in y and s[q] not in y:
                p += 1
                q -= 1
            elif s[p] in y and s[q] not in y:
                q -= 1
            elif s[p] not in y and s[q] in y:
                p += 1
            
            else:
                temp = s[p]
                s[p] = s[q]
                s[q] = temp
                
                p += 1
                q -= 1
        return ''.join(s)
