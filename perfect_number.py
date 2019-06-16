#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:42:15
@LastEditors: Julywaltz
@LastEditTime: 2019-06-16 21:25:47
@Version: $Id$
'''
from math import sqrt


def p_num():
    primes = []
    for num in range(1, 10000000):
        end = int(sqrt(num))
        is_prime = True
        for x in range(2, end + 1):
            if num % x == 0:
                is_prime = False
                break
            if is_prime and num != 1:
                primes.append(num)
    p_nums = []
    for x in primes:
        if 2**x - 1 in primes:
            p_num = (2**x - 1) * 2**(x - 1)
            p_nums.append(p_num)
    print(p_nums)


if __name__ == "__main__":
    p_num()
