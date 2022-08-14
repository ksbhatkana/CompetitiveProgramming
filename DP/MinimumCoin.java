class Solution {
    public int coinChange(int[] coins, int amount) {
        int res[] = new int[amount+1];
        Arrays.fill(res,0);
        res[0]=0;
        for(int i=1;i<=amount;i++)
            res[i] = Integer.MAX_VALUE;
        for (int i=0; i<=amount; i++)
            for (int j=0; j<coins.length; j++){
                if(coins[j]<=i){
                    int subAns = res[i-coins[j]];
                    if(subAns != Integer.MAX_VALUE && subAns+1<res[i])
                        res[i] = subAns +1;
                }
            }
        if(res[amount]==Integer.MAX_VALUE)
            return -1;
        return res[amount];
    }
}
