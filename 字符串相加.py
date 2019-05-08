 def addStrings(self, num1, num2):
  
        len1 = len(num1)
        len2 = len(num2)
        if len2 > len1:
            num1, num2, len1, len2 = num2, num1, len2, len1 
        
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        res = ''
        carry = 0
        for i in range(len1):
            if i < len2:
                val = int(num1[i]) + int(num2[i]) + carry
            else:
                val = int(num1[i]) + carry
                
            carry = val // 10
            val %= 10
            res += str(val)
        
        
        if carry:
            res += '1'
        
        return res[::-1]
