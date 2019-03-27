    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        charDic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K'
                  , 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U'
                  , 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'} 
        
        rstr = ""
        while n != 0:
            if n <= 26:
                rstr = charDic.get(n) + rstr
                n = 0
            else:
                res = n%26
                if res == 0:
                    res = 26
                    n -= 26
                rstr = charDic.get(res) + rstr
                n = n//26
        return rstr
