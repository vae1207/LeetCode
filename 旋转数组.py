    def rotate(self, nums, k):
        """
     
        length = len(nums)
        k = k%length
        for i in range(length-k):
            nums.append(nums.pop(0))
  ####可将列表的前（length-k）个元素先出队，再入队。对于k大于length的情况，可先进行一次k=k%length  ####
  
  
   def rotate(self, nums, k):
  
        while k!= 0:
            temp = nums.pop(-1)
            nums.insert(0,temp)
            k -= 1
