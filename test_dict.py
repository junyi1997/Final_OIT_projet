# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:37:40 2019

@author: user1
"""
saveK1=[]
a={'第01次': {'date_of_birth': 'June 23, 1984', 'sum1': 'Sazae Isono'}, 
   '第02次': {'date_of_birth': 'Aug 23, 1980', 'sum1': 'Masuo Isono'}}
#print(a['user001']['date_of_birth'])
sumi_2=len(a)
print(sumi_2)
for i in range(0,sumi_2):
    if i<9:
        A='第0{:}次'.format(i+1)
        print(A)
    else:
        A='第{:}次'.format(i+1)
    saveK1.append(a[A]['sum1'])
print(saveK1)    