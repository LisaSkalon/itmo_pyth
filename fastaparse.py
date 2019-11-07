#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:05:20 2019

@author: Lisa
"""


    
def translate(rna_seq):

    rna_codon = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
    
    prot = ''
    if (len(rna_seq)%3 == 0):
        for codon in range(0, len(rna_seq), 3):
           prot+=rna_codon[rna_seq[codon:codon+3]]

    return prot
        
def calc_mass(prot_seq):
    
    mass_table = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694,
        'E': 129.04259, 'F': 147.06841, 'G': 57.02146,
        'H': 137.05891, 'I': 113.08406, 'K': 128.09496,
        'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
        'S': 87.03203, 'T': 101.04768, 'V': 99.06841,
        'W': 186.07931, 'Y': 163.06333}
    
    mass = 0
    for aa in prot_seq:
        mass += mass_table[aa]
    return mass

def orf(rna_seq):
    rna_codon = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
    start = ["AUG"]
    stop = ["UAG", "UGA", "UAA"]
    proteins=[]
    sta=0
    stas=[]
    for i in range(len(rna_seq)-3):
        
        if rna_seq[i:(i+3)] in start:
            sta=i
            stas.append(sta)
            
    for start in stas:
        prot=''
        for i in range(start, len(rna_seq)-3, 3):
            if rna_seq[i:(i+3)] in stop:
                break
            prot+=rna_codon[rna_seq[i:(i+3)]]
        proteins.append(prot)
          
    return proteins
    
    