public class Solution {
    public int[] rodCut(int n, int[] prices) {
        int[] dp = new int[n+1];
        for(int i=1; i<=n; i++){
            for(int j=0;j<i;j++){
                dp[i] = Math.max(dp[i], prices[j]+dp[i-j-1]);
            }
        }
        return dp[n];
    }
}
