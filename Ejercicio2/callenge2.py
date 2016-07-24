# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
"""
The program reads the corpus given as the first argument.
Read the testInput also file and divides the body into 
fragments indicated in testInput.
The output displayed for each fragment the three words 
(and their frequency) with a higher frequency.
The program generates a file called "submitOutput" to the output.

USE: python challenge2.py corpus.txt submitInput
"""


def countFrequency(phrase):
	"""
	@brief Function to count the frequency of each word in a sentence.
	@params phrase: array of words
	@returns wreplist: array of words without repeating
	@returns wordlist: array of frequencies of each word wreplist.
	"""
	wordfreq = []

	wordlist = phrase
	wreplist = []
	
	for i in wordlist:
		if i not in wreplist and wordlist.count( i ) >= 1 :
			wreplist.append( i )

	for w in wreplist:
		if wordlist.count( w ) >= 1:
			wordfreq.append( wordlist.count( w ))

	return wreplist, wordfreq


# Read files
manuscript = sys.argv[1]
infile = open(str(manuscript),'r')
text = infile.read()
splitText = text.split(' ')

requeriments = sys.argv[2]
infile2 = open(str(requeriments),'r')
items = int(infile2.readline()) # number of fragments 

# first limit
if items < 1 or items > 5000 :
	print " Error in the number of fragments(1 <= fragment <= 5000) "
 

output = open("submitOutput1",'w')
# for each fragment
for x in range(0, items):

	aux = infile2.readline()
	
	case = x + 1 # number of case

	aux2 = aux.split(' ')
	
	begin = int(aux2[0])
	end = int(aux2[1])
	
	# Second limit
	if ( begin < 1 or begin > 35000 or end < 1 or end > 35000 ):
		print " Error in given for the start (A) or end (B) of the fragments value (1 <= A,B <= 35000)"
	# Fragment selection
	fragment = splitText[begin-1:end]
	dic = {}
	
	# call function
	wreplist, wordfreq = countFrequency(fragment)
	
    # write result
	output.write( str("Case #" + str(case) +": "))
	for i in range(0,len(wreplist)):
		dic[str(wreplist[i])] = wordfreq[i]
	l=dic.items()
	l.sort(key=lambda x: x[1])
	for i in range(1,4):
		if i==3:
			output.write( str( str(l[len(l)- (i)][0]) + " " + str(l[len(l)- (i)][1]) ) )
		else:
			output.write( str( str(l[len(l)- (i)][0]) + " " + str(l[len(l)- (i)][1])+ "," ) )

	output.write("\n")
output.close()

