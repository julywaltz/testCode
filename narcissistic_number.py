#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:41:30
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 14:42:12
@Version: $Id$
'''
#生成水仙花数
n_nums = []
for num in range(100, 1000):
    num_b = num // 100
    num_s = (num - num_b * 100) // 10
    num_g = num - num_b * 100 - num_s * 10
    if num_b**3 + num_s**3 + num_g**3 == num:
        n_nums.append(num)
print(n_nums)