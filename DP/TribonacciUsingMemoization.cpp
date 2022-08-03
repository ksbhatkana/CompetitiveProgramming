class Solution {
public:
    int storage[1000];
    int tribonacci(int n) {
        if(n==0)
            return 0;
        if(n<=2)
            return 1;
        if(storage[n]!=0)
            return storage[n];
        else{
            storage[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
            return storage[n];
        }
    }
};
