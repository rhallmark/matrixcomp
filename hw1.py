#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 00:34:09 2017

@author: Russell

Math 5316 Intro To Matrix Computation
Homework 1

Write a short script that performs a matrix vector product b = Ax using nested
loops. Measure amount of CPU time needed for each to complete.
One should have matrix rows as the outer loop the other should have columns.
Should have a parameter n which determines size of matrix and vector, and
parameter rep for the number of repeats.
"""
import numpy as np

# n = Integer to determin matrix size
# A = a random n x n matrix
# x = a random n x 1 vector
# i = row value of point in matrix
# j = col value of point in matrix
# i,j


def main():
    print "Running ... Homework 1 Script"
    
    choice = '1'
    
    while(choice != '0'):
        print
        print "What would you like to run?:"
        print "a: Matrix rows as outer loop, columns as inner loop"
        print "b: Matrix columns as outer loop, rows as inner loop"
        choice = raw_input(": ")
        print choice
        
        if(choice.lower() == "a"):
            #Execute rows as outer cols as inner
            
            n = raw_input("Define the order (n) of the random matrix A: ")
            try:
                int(n)
            except ValueError:
                print "Provided input is not an integer"
                continue
            
            rep = raw_input("Define the number of repetitions to complete: ")
            try:
                float(rep)
            except ValueError:
                print "Provided input is not a number"
                continue
            
            rowsOuter(n,rep)
            
        elif(choice.lower() == 'b'):
            #Execute cols as outer rows as inner
            pass
        
        else:
            print "Please enter a valid choice!"
            
            
            
            
def createRandSqrMatrix(n, integers=True, low=-50, high=50):
    print "Creating a Random Square Matrix of order " + str(n)
    if(integers==True):
        A = np.random.randint(low, high, (int(n), int(n)))
        print "Matrix A = "
        print A
        return A
    else:
        A = np.random.random((n, n))
        print "Matrix A = "
        print A
        return A
            
def createRandVector(n, integers=True, low=-50, high=50):
    print "Creating a Random Vector x of order " + str(n)
    if(integers==True):
        x = np.random.randint(low, high, (int(n),1))
        print "Vector x = "
        print x
        return x
    else:
        x = np.random.random((n, 1))
        print "Vector x = "
        print x
        return x


    
def rowsOuter(n,rep):
    print "---------------------"
    print "Running Rows Outer..."
    print
    A = createRandSqrMatrix(n)
    print
    x = createRandVector(n)
    print
    
    i_max = n
    j_max = n
    
    #b will be of size n (i-rows) by 1 (j-cols)
    print "Vector b = "
    b = np.zeros(shape=(int(n),1))
    print b
    
    for iteration in rep:
        
        for i in i_max:
            print b(i)
            for j in j_max:
                print "A[i][j] = " + A[i][j]
                print "x[j] = " + x[j]
                b[i] = b[i] + A[i][j] * x[j]
    
    
    print b
    
    print 



def colsOuter():
    print "---------------------"
    print "Running Columns Outer!"
    
    
    print 

    
    
    


if __name__ == "__main__":
    # execute only if run as a script
    main()