#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:44:07
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 14:44:08
@Version: $Id$
'''
#生成斐波拉切数列
a = 0
b = 1
for _ in range(20):
    (b, a) = (a, a + b)
    print(a, end=' ')
