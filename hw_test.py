# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

# Imports
import numpy as np

# Variable Declarations
x = 7
A = np.matrix('8,3,-4;5,1,2;1,2,1')
B = np.matrix('1;2;1')
C = np.matrix('8,3,-4;5,1,2')
D = np.matrix('1,1;2,1;1,1')


# Part 1
print "-----Part 1-----"
print "A ="
print A
print
print "B ="
print B
print
print "Matrix Product of A and B is = "
print np.dot(A,B)
print


# Part 2
print "------Part 2-----"
print "C ="
print C
print
print "D ="
print D
print
print "Matrix Product of C and D is = "
print np.dot(C,D)
print


