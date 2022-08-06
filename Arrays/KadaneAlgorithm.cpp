class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum=-99999, currSum=0;
        for(int i=0;i<nums.size();i++)
        {
            currSum+=nums[i];
            if(currSum>maxSum)
                maxSum=currSum;
            if(currSum<0)
                currSum=0;
        }
        return maxSum;
    }
};

//Kadane's algorithm is used to find longest subarray sum.
