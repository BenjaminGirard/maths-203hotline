#!/usr/bin/env python3
## 203hotline.py for  in /home/tetard/EPITECH_Y2/maths/203hotline
## 
## Made by benjamin girard
## Login   <tetard@epitech.net>
## 
## Started on  Mon Mar 13 10:45:49 2017 benjamin girard
## Last update Thu Mar 23 12:09:07 2017 benjamin girard
##

import sys

from compare_laws import compare_laws
from calc_binomial_coeff import calc_binomial_coeff

def check_int(string):
    try:
        i = int(string)
        return i
    except ValueError:
        sys.exit(84)

def handle_args():
    res = []
    args = sys.argv
    if len(args) != 2 and len(args) != 3:
        sys.exit(84)
    for arg in args[1:3]:
        res.append(check_int(arg))
    return res

if __name__ == '__main__':
    args = handle_args()
    if len(args) == 1:
        compare_laws(args[0])
    else:
        calc_binomial_coeff(args[0], args[1])
