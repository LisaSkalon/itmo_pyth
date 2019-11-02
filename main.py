#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:11:47 2019

@author: gospozha
"""

import mycsv

lines = mycsv.read_csv("data.csv")
lines_commas = mycsv.read_csv("data_commas.csv")
lines_stars = mycsv.read_csv("data_stars.csv", sep='*')

lines = [
    ['ID', 'Vlaue'], 
    ['101', '10,5'], 
    ['102', '11'],
    ['103','11.5']
    ]

mycsv.write_csv("data_1.csv", lines)
mycsv.write_csv("data_1.tsv", lines, sep="\t")
