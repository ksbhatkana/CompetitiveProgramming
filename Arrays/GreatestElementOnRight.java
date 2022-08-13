class Solution {
    public int[] replaceElements(int[] arr) {
        System.out.print(arr.length-1);
        int res[] = new int[arr.length];
        res[arr.length-1] = arr[arr.length-1];
        for(int i = arr.length-2;i>=0;i--){
            res[i] = Math.max(arr[i+1],res[i+1]);
        }
        res[arr.length-1] = -1;
        return res;
    }
}
