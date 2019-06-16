# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 03:37:40 2018

@author: Rishi
"""

import matinput as m
mult=m.np.zeros((m.n1,m.n1))
for i in range(len(m.mat1)):
    for j in range(len(m.mat2)):
        for k in range(len(m.mat2)):
            mult[i][j]+=m.mat1[i][k]*m.mat2[k][j]
            
print("PRODUCT OF MATRICES IS: \n",mult)
