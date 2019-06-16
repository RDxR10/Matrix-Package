# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 03:10:46 2018


"""

#Take matrix size as input
n1=int(input("Enter the matrix size: "))
print("ENTER THE MATRIX ELEMENTS SEPARATED BY SPACE AND NEXT LINE AFTER EACH",n1,"ELEMENTS")
import numpy as np
#initialize nxn matrix with zeroes
mat1=np.zeros((n1,n1))
#input each row at a time, with each element separated by a space
for i in range(n1):
    mat1[i]=input().split(" ")
print(mat1)
mat2=np.zeros((n1,n1))
print("Enter the second matrix")
for i in range(n1):
    mat2[i]=input().split(" ")
print(mat2)
