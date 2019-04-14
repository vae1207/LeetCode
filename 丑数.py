class Solution(object):
    def isUgly(self, num):
     
        if num <= 0:
            return False
        else:
            num_copy = num
            while True:
                if (num % 2) == 0:
                    num /= 2
                if (num % 3) == 0:
                    num /= 3
                if (num % 5) == 0:
                    num /= 5
                
                if num == 1:
                    return True
                if num_copy == num:
                    return False
                else:
                    num_copy= num
