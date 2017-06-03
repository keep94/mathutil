# mathutil

Math utilities in python

# Introduction

This library contains miscellaneous math functions.

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
