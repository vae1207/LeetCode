class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n<=0)
            return false;
        if(n>1){
            if(n%2 == 0){
                n /=2;
                return isPowerOfTwo(n);
            }
            else
                return false;
        }
        return true;
    }
}
