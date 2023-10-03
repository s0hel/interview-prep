package com.s0hel.recursion;

public class Fibonacci {

    public int fib(int n) {
        if (n <= 1) {
            return n;
        }

        //return fib(n-1) + fib(n-2);
        int prev = 1, prev2 = 0;
        int sum = prev + prev2;
        for (int i = 2; i < n; ++i) {
            prev2 = prev;
            prev = sum;

            sum = prev + prev2;
        }

        return sum;
    }

}
