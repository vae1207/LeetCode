class Solution(object):
    def toHex(self, num):
        
        dict = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexRes = []
        if num<0:
            num += 2**32
        if num == 0:
            return '0'
        while num > 0:
            figure = num %16
            num /= 16
            if figure>=0 and figure<=9:
                hexRes.append(str(figure))
            else:
                hexRes.append(dict[figure])
        hexRes = hexRes[::-1]
        return ''.join(hexRes)
