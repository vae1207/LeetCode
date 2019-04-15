class Solution(object):
    def firstBadVersion(self, n):
    "二分法"
        L,R = 1,n
        while L < R:
            mid = (L+R)/2
            
            if not isBadVersion(mid):
                L = mid + 1
            else:
                R = mid
        return R
