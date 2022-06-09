class Solution {
    public int rob(int[] nums) {
        //Tabulation dp: O(n)
        int n= nums.length;
        int[] dp= new int[n];
        dp[0]=nums[0];
        for(int i=1; i<n; i++){
            
            int op1= dp[i-1];
            int op2= (i>1) ? dp[i-2]+ nums[i] : nums[i];
            dp[i]= Math.max(op1,op2);
        }
        
        return dp[n-1];        
    }
}