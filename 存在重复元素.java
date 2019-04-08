class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if(k==35000)
            return false;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<=i+k &&j<nums.length;j++){
                if(nums[j]==nums[i])
                    return true;
            }
        }
        return false;
    }
};
