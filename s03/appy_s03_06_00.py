#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:39:39 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.linspace (0.0, 10.0, 11)

# printing A
print (f'a:\n{a}')

# accessing to an element by indexing
print (f'a[0]  = {a[0]}')
print (f'a[1]  = {a[1]}')
print (f'a[5]  = {a[5]}')
print (f'a[-1] = {a[-1]}')
print (f'a[-3] = {a[-3]}')
