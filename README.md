# mathutil

Math utilities in python

# Introduction

This library contains miscellaneous math functions.

# Theory

## The cake problem

The cake problem asks how many pieces can you get if you cut an n dimensional
cake k times.  This problem can be solved using dynamic programming.

Let c(n, k) be the number of pieces you get cutting an n dimensional cake k
times.

A 0 dimensional cake is just 1 piece no matter how many times it is cut, so
c(0, k) = 1.

Now to compute c(n, k);

When making that kth cut in an n dimensional cake, the cross section of the
cut will have n-1 dimensions and will have k-1 cuts in it from the previous
k-1 cuts. So making that kth cut adds c(n-1, k-1) more pieces. To the
c(n, k-1) pieces from the previous k-1 cuts.

So c(n, k) = c(n, k-1) + c(n-1, k-1)

### Another way to think of the cake problem.

We claim that c(0, k) is a 0th degree polynomial of k (it is the constant 1).
We claim that c(1, k) is a 1st degree polynomial of k.
We claim that c(2, k) is a 2nd dgree polynomial of k etc.

Thinking about our formula c(n, k) = c(n, k-1) + c(n-1, k-1) we see that
c(3, k) is a 3rd degree polynomial of k because it is just a summation of
the c(2, k) terms.

In general c(n, k) is an nth degree polynomial of k.

We know that c(n, k) is 2^k when k <= n (cutting a 3 dimensional cake 2 times
gives 4 slices; cutting a 3 dimensional cake 3 times gives 8 slices).
We also know that the summation of nCk as k goes from 0 to n is 2^n.
We also know that nCk is a kth degree polynomial of n.
nCk means n choose k, the number of ways to choose k items from n items where
order doesn't matter.

Therefore c(n, k) = kC0 + kC1 + kC2 + ... + kCn

This formula makes c(n, k) be an nth degree polynomial of k and it ensures
that c(n, k) = 2^k for k <= n

# The python code

## p = mathutil.CPoly(x); p(n)

mathutil.CPoly computes (n + x - 1) C x. x can be any real number; n must be an
integer >= 0. p caches results, so its best to reuse p when possible.

The example below computes (4 + 2 - 1) C 2 = 5 C 2

```
>>> p = mathutil.CPoly(2); p(4)
10.0
```

## u = mathutil.Ugly(*primeFactors); u(n)

mathutil.Ugly computes the nth number whose prime factors are a subset of
primeFactors. The values in primeFactors must be prime numbers, and n must
be an integer >= 1. u caches results, so it is best to reuse u when possible.

Note that u(1) = 1 regardless of the values in primeFactors because 1 has no
prime factors

The first 16 numbers whose prime factors are a subset of [2, 3, 5] are
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, ...

The example below computes the 16th number whose prime factors are
among 2, 3, and 5

```
>>> u = mathutil.Ugly(2,3,5); u(16)
25
```

## c = mathutil.Cake(); c(n, k)

mathutil.Cake computes how many pieces you can get if you cut an n dimensional
cake k times. n and k must be integers >= 0. c caches results, so it is best
to reuse c when possible.

The example below computes that if you cut a 3 dimensional cake 4 times, you
can get up to 15 pieces.

```
>>> c = mathutil.Cake(); c(3, 4)
15
```

## p = mathutil.Partition(); p(n)

mathutil.Partition is the partition function which calculates how many ways
n can be partitioned when order doesn't matter. For example:

p(4) = 5 because 4 can be partitioned 5 ways where order doesn't matter

4 = 1 + 1 + 1 + 1
4 = 1 + 1 + 2 (covers 2 + 1 + 1 and 1 + 2 + 1)
4 = 1 + 3 (covers 3 + 1)
4 = 2 + 2
4 = 4

n must be an integer >= 0. p caches results, so it is best to reuse p when
possible.
