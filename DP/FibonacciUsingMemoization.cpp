class Solution {
public:
    int storage[1000];
    int fib(int n) {
        if (n<=1)
            return n;
        if(storage[n]!=0)
            return storage[n];
        else
            storage[n]= fib(n-1) + fib(n-2);
            return storage[n];
    }
};
