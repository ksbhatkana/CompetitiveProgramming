class Solution {
    public int majorityElement(int[] nums) {
        int num=nums[0];
        int count = 1;
        for(int i=1;i<nums.length;i++){
            if(nums[i] == num)
                count++;
            else{
                count--;
                if(count<0){
                    count = 0;
                    num=nums[i];
                }
            }
        }
        count =0;
        System.out.print(num);
        for(int i=0;i<nums.length;i++){
            if(nums[i]==num)
                count++;
            if(count>nums.length/2)
                return num;
        }
        return -1;
    }
}
