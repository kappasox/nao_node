#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sample Implemantation of IPUT Course 
# IoT Device Programming 2 (2024 Winter)
# Week 07
#
# IPUT Math Library
# - It is not enoguh math library,
#   but it can be used for studying modules or data structures.
#
# Nov. 7, 2024
# Michiharu Takemoto (takemoto.development@gmail.com)
#
#
# MIT License
# 
# Copyright (c) 2024 Michiharu Takemoto <takemoto.development@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# 
#

def simple_get_average01(data_l):
    count = 0
    n_times = len(data_l)
    sum = 0

    while (True):
        sum = sum + data_l[count]
        count = count + 1
        if (count > n_times - 1):
            break

    average = sum / n_times

    return average


def simple_get_average02(data_l):
    sum = 0

    for d in data_l:
        sum = sum + d

    average = sum / len(data_l)

    return average


class iput_math_class:

    def __init__(self) -> None:
#        print('initializer is called.')
        pass

    def get_avarage(self, data_l):
        if (data_l == []):
            raise NoDataError
        
        count = 0
        n_items = len(data_l)
        sum = 0

        data_type0 = type(data_l[0])

        while(True):
            sum = sum + data_l[count]

            data_type = type(data_l[count])
            if (data_type is not data_type0):
                raise TypeUnmatchError
            count = count + 1
            if (count > n_items - 1):
                break

        average = sum / n_items

        return average

class IPUTException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.args = args

class NoDataError(IPUTException):
    def __str__(self) -> str:
        return('(IPUT) No data in the List!')
    
class TypeUnmatchError(IPUTException):
    def __str__(self) -> str:
        return('(IPUT) Data types are not matched!')
    

if '__main__' == __name__ :

    calc_instance = iput_math_class()

    print('--------------')
    x = [10, 20, 30, 40]
    print(x)
    y = calc_instance.get_avarage(x)
    print(y)

    print('--------------')
    x = [10, 20, 30, 40]
    print(x)
    try:
        y = calc_instance.get_avarage(x)
        print(y)
    except NoDataError as e:
        print(e)

    print('--------------')
    x = []
    print(x)
    try:
        y = calc_instance.get_avarage(x)
        print(y)
    except NoDataError as e:
        print(e)
    except TypeUnmatchError as e:
        print(e)

    print('--------------')
    x = [10, 20, 30.0, 40]
    print(x)
    try:
        y = calc_instance.get_avarage(x)
        print(y)
    except NoDataError as e:
        print(e)
    except TypeUnmatchError as e:
        print(e)

    print('--------------')
    x = []
    print(x)
    try:
        y = calc_instance.get_avarage(x)
        print(y)
    except (NoDataError,
            TypeUnmatchError) as e:
        print(e)

    print('--------------')
    x = [10, 20, 30.0, 40]
    print(x)
    try:
        y = calc_instance.get_avarage(x)
        print(y)
    except (NoDataError,
            TypeUnmatchError) as e:
        print(e)

    print('--------------')
    x = [1, 2, 3, 4]
    print(x)
    y = simple_get_average01(x)
    print(y)

    print('--------------')
    x = [1, 2, 3, 4.2, 5]
    print(x)
    y = simple_get_average02(x)
    print(y)

    # print('--------------')
    # x = []
    # print(x)
    # y = simple_get_average02(x)
    # print(y)

