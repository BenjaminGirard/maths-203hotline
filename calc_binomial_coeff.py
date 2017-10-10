#!/usr/bin/env python3.3
## calc_binomial_coeff.py for  in /home/tetard/EPITECH_Y2/maths/203hotline
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Mon Mar 13 10:58:10 2017 benjamin girard
## Last update Thu Mar 23 12:12:17 2017 benjamin girard
##

import sys
from math import factorial

def calc_binomial_coeff(n, k):
    if n < k:
        sys.exit(84)
    res = factorial(n) // (factorial(k) * factorial(n - k))
    print("{k}-combination of a {n} set:\n{res}".format(k=k, n=n, res=res))
