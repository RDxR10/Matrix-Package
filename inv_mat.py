# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 03:14:13 2018

@author: Rishi
"""
import matinput as m
m1_inv = m.np.linalg.inv(m.mat1)
m2_inv = m.np.linalg.inv(m.mat2)
print("INVERSE OF THE MATRIX 1 IS: \n",m1_inv)
print("INVERSE OF THE MATRIX 2 IS: \n",m2_inv)
