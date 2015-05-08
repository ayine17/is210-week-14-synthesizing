#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1."""


def xfibo(count):
    """ fibonancci function
    args:
        count(int): The number of Fibonacci numbers to return
    return:
        return number of Fibonacci numbers
    example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """

    counter = 0
    lastnum, curnum = 0, 1
    while counter < count:

        yield lastnum
        counter += 1

        lastnum, curnum = curnum, lastnum + curnum
