#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week14 task_02"""


import task_01


def fibo(count):
    """ function to create Fibonacci numbers
    args:
        count(int): The total number of Fibonacci numbers to return
    return:
        return number of Fibonacci numbers
    exmple:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """

    numbers = []
    for i in task_01.xfibo(count):
        numbers.append(i)
    return numbers
