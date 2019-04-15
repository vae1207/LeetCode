class Solution(object):

    def moveZeroes(self,nums):
          
          slen = len(nums)
          l,r = 0, slen-1
          while l!= r:
               if nums[l] == 0:
                  nums.append(0)
                  del nums[l]
                  r -= 1
               else:
                  l += 1
               print(l,r)
          return nums
