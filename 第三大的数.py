class Solution(object):
    def thirdMax(self, nums):
       
        nums.sort(reverse = True)
        step = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                step += 1
            if step == 2:
                return nums[i+1]
        if step == 0 or step == 1:
            return nums[0]
