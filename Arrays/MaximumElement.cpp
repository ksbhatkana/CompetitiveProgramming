//This solution solves problem in O(n) time complexity and O(1) space complexity
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int numIndex=0;
        int count=1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[numIndex]==nums[i])
                count++;
            else
                count--;
            if(count==0)
            {
                numIndex=i;
                count=1;
            }
        }
        // return nums[numIndex]; // IF question guarantees max element exists always, then return here. Otherwise below loop is important.
        count=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==nums[numIndex])
                count++;
        }
        if(count>=nums.size()/2)
            return nums[numIndex];
    }
};
