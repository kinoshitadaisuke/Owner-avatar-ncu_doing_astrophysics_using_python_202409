#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/24 20:44:32 (UT+8) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

# printing "a"
print (f'a:\n{a}')

# sorting
b = numpy.sort (a)

# printing "b"
print (f'b = numpy.sort (a):\n{b}')
