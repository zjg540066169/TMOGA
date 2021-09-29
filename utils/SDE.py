#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Provide function to calculate SDE distance

@auth: Jungang Zou
@date: 2021/05/05
"""

def SDE(front, values1, values2):
    shifted_dict = {}
    for i in front:
        shifted_dict[i] = [(values1[i], values2[i])]
        shifted_list = []
        for j in front:
            if i == j:
                continue
            else:
                shifted_list.append((min(values1[i], values1[j]), min(values2[i], values2[j])))
        shifted_dict[i].append(shifted_list)
    return shifted_dict
            