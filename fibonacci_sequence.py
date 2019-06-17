#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:44:07
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 15:08:08
@Version: $Id$
'''


def f_num():
  '''
  生成斐波那契数列
  '''
  a = 0
  b = 1
  for _ in range(20):
    (b, a) = (a, a + b)
    print(a, end=' ')


if __name__ == "__main__":
  f_num()
