class solution:
    def reverseBits(self,n):
        res = '{0:032b}'.format(n)
        res = res[::-1]
        res = int(res,2)
        
        return res
