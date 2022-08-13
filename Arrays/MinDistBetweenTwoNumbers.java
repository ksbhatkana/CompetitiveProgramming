class Solution {
     int minDist(int a[], int n, int x, int y) {
       
       if(x == y) return -1;
       int j = -1;
       int k = -1;
       int min = Integer.MAX_VALUE;
       for(int i = 0  ; i < n ; i++)
       {
           if(a[i] == x) j = i;
           if(a[i] == y) k = i;
           
           if(k != -1 && j != -1){
           
           int dis = k>j?k-j:j-k;
           min = Math.min(min , dis);
           
           }
       }
       
       if(j == -1 || k == -1) return -1;
       return min;
       
   }
}
