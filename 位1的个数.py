class solution:
   def hammingWeight(self,n):
      result = 0
      detector = 1
      for i in range(32):
          if n & detector:
              result += 1
          detector = detector << 1
      return result
