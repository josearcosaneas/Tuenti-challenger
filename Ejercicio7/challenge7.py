# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import string

def convert(x):
	r = 1000
	if x == 'A':
		r = 1
	elif  x=='a':
		r = -1
	elif  x == 'B':
		r = 2
	elif  x=='b':
		r = -2
	elif  x == 'C':
		r = 3
	elif  x=='c':
		r = -3	 	 
	elif  x == 'D':
		r = 4
	elif  x=='d':
		r = -4
	elif x == 'E':
		r = 5
	elif x=='e':
		r = -5
	elif  x == 'F':
		r = 6
	elif  x=='f':
		r = -6
	elif  x == 'G':
		r = 7
	elif  x=='g':
		r = -7
	elif  x == 'H':
		r = 8
	elif  x=='h':
		r = -8
	elif  x == 'I':
		r = 9
	elif  x=='i':
		r = -9
	elif  x == 'J':
		r = 10
	elif  x=='j':
		r = -10
	elif  x == 'K':
		r = 11
	elif  x=='k':
		r = -11
	elif  x == 'L':
		r = 12
	elif  x=='l':
		r = -12
	elif  x == 'M':
		r = 13
	elif x=='m':
		r = -13
	elif  x == 'N':
		r = 14
	elif  x=='n':
		r = -14
	elif  x == 'O':
		r = 15
	elif  x=='o':
		r = -15
	elif x== 'P':
		r = 16
	elif x== 'p':
		r = -16
	elif x == 'Q':
		r = 17
	elif  x=='q':
		r = -17
	elif x == 'R':
		r = 18
	elif x=='r':
		r = -18
	elif x == 'S':
		r = 19
	elif x=='s':
		r = -19
	elif x == 'T':
		r = 20
	elif x=='t':
		r = -20
	elif x == 'U':
		r = 21
	elif x=='u':
		r = -21
	elif x == 'V':
		r = 22
	elif x=='v':
		r = -22
	elif x == 'W':
		r = 23
	elif x=='w':
		r = -23
	elif x == 'X':
		r = 24
	elif x=='x':
		r = -24
	elif x == 'Y':
		r = 25
	elif x=='y':
		r = -25
	elif x == 'Z':
		r = 26
	elif x=='z':
		r = -27
	elif x=='.':
		r = 0
	return r

def transformMatrix(matrix):
	out_2 = []
	
	for i in range(0, len(matrix)):
		out = []
		for j in range(0,len(matrix[i])):
				
				out.append(convert(matrix[i][j]))
		out_2.append(out)
	return out_2


# prints the maximum "area" given by the values of an NxM array inside a
# subarray with dimensions maxRows x maxCols. temp holds the latest vector to be
# given to kadane1DwithBounds()
def kadane2DwithBounds(maxRows, maxCols):
    global temp
    for i in xrange(N):
        temp[i] = sum(table[i][j] for j in xrange(maxCols))

    m = kadane1DwithBounds(maxRows)

    k = 0
    for j in xrange(1, M - maxCols + 1):
        for i in xrange(N):
            temp[i] -= table[i][k]
            temp[i] += table[i][maxCols + j - 1]
        k += 1
        m = max(m, kadane1DwithBounds(maxRows))

    return m

def SumRectangle(rectangle):
	sum = 0
	for i in range(0,len(rectangle)):
		for j in range(0, len(rectangle[0])):
			sum = rectangle[i][j]

	return sum

infile = open(sys.argv[1],"r")

n = infile.readline()#numero de casos
n_aux = 0
 
# Para cada caso
while n_aux !=int(n):
	matrix = []
	tam = infile.readline().split()
	
	# read matrix
	for i in range(0,int(tam[0])):
		row = infile.readline().split()[0]
		row_1 = []
		for k in range(0,len(row)):
			
			row_1.append(row[k])
		
		matrix.append(row_1)

	
	n_aux=n_aux+1
	if len(matrix) == 2 and len(matrix[0])==2:
		print "Case #"+str(n_aux)+": INFINITY"
	elif len(matrix) == 1 and len(matrix[0])==1:
		print "Case #"+str(n_aux)+": 0"
	else:
		print "Case #"+str(n_aux)+":"+str(SumRectangle(transformMatrix(matrix)))
	

