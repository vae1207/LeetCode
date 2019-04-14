class Solution(object):
    def addDigits(self, num):
      
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num

    
    方法二:
 class Solution(object):
    def addDigits(self, num):
  
        if num == 0:
            return  0
        if num%9 == 0:
            return 9
        else:
            return num % 9
