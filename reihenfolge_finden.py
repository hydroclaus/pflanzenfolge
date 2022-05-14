#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hello
"""
import sys
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

__author__ = "Claus Haslauer (mail@planetwater.org)"
__version__ = "$Revision: 0.1 $"
__date__ = datetime.date(2022,5,13)
__copyright__ = "Copyright (c) 2021 Claus Haslauer"
__license__ = "Python"


def calc_performance_this_series(indices, i, pflanzen_uebergangs_matrix):
    n = len(i)
    this_series = 0
    for ix in range(0,n-1):
        # print(indices[ix]-1, indices[ix+1])
        # print(pflanzen_uebergangs_matrix[indices[ix]-1,indices[ix+1]])
        # print(np.isfinite(pflanzen_uebergangs_matrix[indices[ix]-1, indices[ix+1]]))
        if np.isfinite(pflanzen_uebergangs_matrix[indices[ix]-1, indices[ix+1]]):
            cur_val = pflanzen_uebergangs_matrix[indices[ix]-1, indices[ix+1]]        
        else:
            cur_val = pflanzen_uebergangs_matrix[indices[ix+1]-1, indices[ix]]
        this_series += cur_val
        #print(cur_val)
        #print("---")
    print("  hat eine Wertigkeit von: ", this_series)
    return this_series

def main():
    plt.ioff()
    print("Let's start!")

    # dafuer suche ich die beste reihenfolge
    suche_max_fuer = ['Tomate', 'Spargel', 'Mangold']

    # in der csv steht, was gut passt
    fname = r'Pflanzenfolge_Tabelle.csv'

    # lese nur die Pflanzennamen ein, die in der Liste stehen
    gelistete_pflanzen = np.genfromtxt(fname,
                                   delimiter=",",
                                   dtype=None,
                                   encoding=None)[0,1:]
    print("diese Pflanzen kommen in der Uebergangsmatrix vor:")
    print(gelistete_pflanzen)
    print("")

    # lese die Uebergangsmatrix ein
    pflanzen_uebergangs_matrix = np.genfromtxt(fname,
                                           delimiter=",")[2:,1:]
    print("so schaut die uebergangsmatrix aus:")
    print(pflanzen_uebergangs_matrix)
    print("")
    
    for i in list(permutations(suche_max_fuer)):
        print("betrachte Kombination: ", i)
        sorter = np.argsort(gelistete_pflanzen)
        indices = sorter[np.searchsorted(gelistete_pflanzen, i, sorter=sorter)]
        #print(indices)
        calc_performance_this_series(indices, i, pflanzen_uebergangs_matrix)


    
    print("\nDone! Yay!")
if __name__ == '__main__':
    main()