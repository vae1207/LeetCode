class Solution(object):
    def intersect(self, nums1, nums2):
 
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i),nums2.count(i))
        return l
