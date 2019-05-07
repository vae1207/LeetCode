class Solution(object):
    def fizzBuzz(self, n):
        
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res += ['FizzBuzz']
            elif i % 3 == 0:
                res += ['Fizz']
            elif i % 5 == 0:
                res += ['Buzz']
            else:
                res.append(str(i))
        return res
