# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Method resolution:

We need to know the number of tables taken a number n.

For n <= 4 the number of tables will be 1.
For n = 5 or n = 6 the number of tables will be 2.
For n = 7 and n = 8 the number of table will be in March.
...
We can guess that we have a sequence of integers.

Since n:
- If n is even:
the solution is given by the function:
x = n / 2 - 1
- If n is odd:
x = n / 2

USE:

python challenge1.py testInput > testOutput


WHERE:

challenger1.py is the source code.
testInput is the data file in the correct format.
testOutput  is the output file.
"""
import sys



ffile = sys.argv[1] 
infile = open(str(ffile),'r')
items = int(infile.readline())

i = 1

# First limit
if items < 1 or items > 50:
	print "Error : 1 <= T <= 50"
	

for x in range(0,int(items)):
		
	aux = int(infile.readline())

	# Second limit
	if aux <= 0 or aux >= 65536:
		print "Case #" + str(i) + ": " + str(0)
		i = i+1

	elif aux > 0 and aux <= 4 and aux < 65536:
		print "Case #" + str(i) + ": " + str(1)
		i = i +1

	elif aux > 0 and aux%2 == 0 and aux < 65536:
		n = aux/2 - 1
		print "Case #" + str(i) + ": " + str(n)
		i= i+1

	elif aux > 0 and aux%2 != 0 and aux < 65536:
		n = int(aux/2)
		print "Case #" + str(i) + ": " + str(n)
		i = i+1
	else:
		break;
