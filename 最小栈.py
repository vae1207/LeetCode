class MinStack(object):

   def __init__(self):
      
      self.l = []
   
   
   def push(self,x):
      
      if x is None:
          pass
      else:
          self.l.append(x)
   
   def pop(self,x):
      
      if self.l is None:
          return 'error'
      else:
          self.l.pop(-1)
   
   def top(self):
      
      if self.l is None:
          return 'error'
      else:
          return self.l[-1]
   
   
   def getMin(self):
      
      if self.l is None:
          return 'error'
      else:
          return min(self.l)
   
