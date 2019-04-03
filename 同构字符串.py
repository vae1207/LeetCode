class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """      
        l = len(s)
        if l == 0 or l == 1:
            return True
        d = {t[0]:s[0]}
        for i in range(1, l):
            if s[i] == s[i-1]:
                if t[i] == t[i-1]:
                    continue
                else:
                    return False
            else:
                if t[i] in d:
                    if d[t[i]] == s[i]:
                        continue
                    else:   
                        return False
                else:
                    d[t[i]] = s[i]
        return True
