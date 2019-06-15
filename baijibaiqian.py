#!/usr/bin/env python
# -*- coding=utf-8 -*-
'''
@Author: Julywaltz
@Date: 2019-06-15 14:43:03
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 15:15:20
@Version: $Id$
'''


def baijibaiqian():
    '''
    解百鸡百钱问题
    '''
    ans = []
    for cock in range(0, 100):
        for hen in range(0, 100):
            if 5 * cock + 3 * hen + (100 - cock - hen) / 3 == 100:
                ans.append({'公鸡': cock, '母鸡': hen, '小鸡': 100 - cock - hen})
    print(ans)


if __name__ == "__main__":
    baijibaiqian()
