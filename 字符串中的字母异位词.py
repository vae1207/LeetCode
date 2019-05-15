class Solution(object):
    def findAnagrams(self, s, p):
      
        dict_p = {}
        for i in p:
            dict_p[i] = dict_p.get(i,0) + 1
        dict_s = {}
        list_n = []
        len_p = len(p)
        for i,val in enumerate(s):
            dict_s[val] = dict_s.get(val,0) + 1
            if dict_s == dict_p:
                list_n.append(i - len_p + 1)
            if i - len_p + 1 >=0:
                dict_s[s[i-len_p+1]] = dict_s.get(s[i-len_p +1]) -1
                if dict_s[s[i- len_p + 1]] == 0:
                    del dict_s[s[i-len_p+1]]
        return list_n
