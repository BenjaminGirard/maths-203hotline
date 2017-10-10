#!/usr/bin/env python3.3
## compare_laws.py for h in /home/tetard/EPITECH_Y2/maths/203hotline
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Mon Mar 13 10:52:03 2017 benjamin girard
## Last update Thu Mar 23 13:57:34 2017 benjamin girard
##

import sys
import time

from math import factorial, exp

def calc_distrib(coeff, n):
    off = n
    res = 1
    while off > (n - coeff):
        res = res * off
        off -= 1
    return (res / factorial(coeff))

def print_binomial(av):
    print("Binomial distribution:")
    av = (((av / 3600.0) * 3500.0) / 8) / 3500
    distrib = []
    res = 0
    off = 0
    perf = time.time()
    while (off <= 100):
        tmp = calc_distrib(off, 3500) * (av**off) * \
              (1.0 - av)**(3500 - off)
        if (((off + 1) % 6) == 0 or off == 50) and off <= 50:
            print("{off} -> %.3f".format(off=off) % tmp)
        else:
            if off <= 50:
                print("{off} -> %.3f\t".format(off=off) % tmp, end="")
        if off > 25:
            res += (tmp * 100)
        off += 1
        distrib.append(tmp)
    print("overload: %.1f%%" % res)
    perf = (time.time() - perf) * 1000
    print("computation time: %.2f ms" % perf)


def print_poisson(av):
    print("Poisson distribution")
    av = ((av / 3600.0) * 3500.0) / 8
    off = 0
    res = 0
    distrib = []
    perf = time.time()
    while off <= 100:
        tmp = (pow(av, off) * exp(-av)) / factorial(off)
        if ((off + 1) % 6 == 0 or  off == 50) and off <= 50:
            print("{off} -> %.3f".format(off=off) % tmp)
        else:
            if off <= 50:
                print("{off} -> %.3f\t".format(off=off) % tmp, end="")
        if off > 25:
            res += (tmp * 100)
        distrib.append(tmp)
        off += 1
    print("overload: %.1f%%" % res)
    perf = (time.time() - perf) * 1000
    print("computation time: %.2f ms" % perf)


def compare_laws(average):
    print_binomial(average)
    print("")
    print_poisson(average)
