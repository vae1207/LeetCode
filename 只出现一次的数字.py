def singleNumber(self, nums)

  a = 0
  for num in nums:
    a = a ^ num
  return a
