#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:26:56 2019

@author: Lisa
"""

import os.path
import re

def read_csv(path_to_csv_file, sep=","):
    if os.path.exists(path_to_csv_file) == False:
        print('Error, such file does not exist')
        return []
    else:
        with open(path_to_csv_file, 'r') as f:
                data = [line.rstrip().split(sep) for line in f]
                for string in data:
                    for index, word in enumerate(string):
                        if re.match(r"\"\w+$", word) != None:
                            string.insert(index, string[index][1:len(string[index])]+sep+string[index+1][0:len(string[index+1])-1])
                            del string[index+1]
                            del string[index+1]
        return(data)
    
def write_csv(path_to_csv_file, data, sep=','):
    try:
        with open(path_to_csv_file,'w') as f:
           for string in data:
               for index, word in enumerate(string):
                   if ('.' in word) or (',' in word):
                       f.write('"'+word+'"')
                   else:
                       f.write(word)
                   if index != (len(string)-1):
                       f.write(sep)
               f.write('\n')
        return(path_to_csv_file)
    except Exception as error:
        print(error)
        return(path_to_csv_file)
    
        
#read_csv('doc.csv', ':')  
#
#lines = [
#    ['ID', 'Vlaue'], 
#    ['101', '10,5'], 
#    ['102', '11'],
#    ['103','11.5']
#    ]
#write_csv("data_1.csv", lines)     
#
#with open("data_1.csv",'w') as f:
#       for string in lines:
#           for index, word in enumerate(string):
#               if ('.' in word) or (',' in word):
#                   f.write('"'+word+'"')
#               else:
#                   f.write(word)
#               if index != (len(string)-1):
#                   f.write(',')
#           f.write('\n')
        
#import re        
#cont=[]        
#with open('data_commas.csv') as d:
#    cont = [line.rstrip().split(',') for line in d]
#    for string in cont:
#        for index, el in enumerate(string):
#            if re.match(r"\"\w+$", el) != None:
#                string.insert(index, string[index][1:len(string[index])]+','+string[index+1][0:len(string[index+1])-1])
#                del string[index+1]
#                del string[index+1]
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        