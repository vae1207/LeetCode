class Solution(object):
    def containsDuplicate(self, nums):
    
    
        set1 = set(nums)
        if len(set1) == len(nums):
            return False
        else:
            return True 
