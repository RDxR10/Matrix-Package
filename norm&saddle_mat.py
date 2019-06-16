# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 03:50:30 2018


"""

import matinput as m
z = m.mat1
z1 = m.mat2
nn = m.n1
print("FROBENIUS NORM OF MATRIX 1 IS:")
print(m.np.linalg.norm(z,ord='fro',axis=None,keepdims=False))
print("FROBENIUS NORM OF MATRIX 2 IS:")
print(m.np.linalg.norm(z1,ord='fro',axis=None,keepdims=False))


rowmins = []
rowmaxs = []
colmins = []
colmaxs = []
l1=[]
l2=[]
l3=[]
l4=[]

    
for i,row in enumerate(z):
    m = min(row)
    M = max(row)
    for j,x in enumerate(row):
            if x == m: rowmins.append((i,x))
            if x == M: rowmaxs.append((i,x))

    t = [list(column) for column in zip(*z)] #transpose of matrix

    for j,col in enumerate(t): 
        m = min(col)
        M = max(col)
        for i,x in enumerate(col):
            if x == m: colmins.append((j,x))
            if x == M: colmaxs.append((j,x))

for i in rowmins:
    l1.append(i[1])
    for j in colmaxs:
        l2.append(j[1])

if max(l1)==min(l2):
    print("SADDLE POINT considering ROWMINS AND COLMAXS IS: ",max(l1))
else:
    print("NO SADDLE POINT")
    
for k in rowmaxs:
    l3.append(k[1])
for l in colmins:
    l4.append(l[1])
if min(l3)==max(l4):
    print("SADDLE POINT considering ROWMAXS AND COLMINS IS: ",min(l3))
else:
    print("NO SADDLE POINT")
    
    
        
        
    
        
   



            
