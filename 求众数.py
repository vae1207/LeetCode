    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt,ret = 0,0
        for num in nums:
            if cnt == 0:
                ret = num
            if num != ret:
                cnt -= 1
            else:
                cnt += 1
            
        return ret

    
    
 或者：
    def majorityElement(self,nums):
         
        nums.sort()
        return nums[len(nums)/2]
