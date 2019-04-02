class solution:
  def isHappy(self,n):
      
      
      l = []
      while True:
        l.append(n)
        n = sum([int(i)**2 for i in str(n)])
        if n == 1:
          return False
        elif n in l:
          return True
