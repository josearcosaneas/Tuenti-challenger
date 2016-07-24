# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
import sys




combos = []

patrones1 = []
patron1 = re.compile(r'L-LD-D-RD-R')
patron11 = re.compile(r'\bL-LD-D-RD-R-[^P]\b')
patrones1.append(patron1)
patrones1.append(patron11)

patrones2 = []
patron2 = re.compile(r'\bD-RD-R\b')
patron22 = re.compile(r'\bD-RD-R-[^P]\b')
patrones2.append(patron2)
patrones2.append(patron22)

patrones3 = []
patron3 = re.compile(r'\bR-D-RD\b')
patron33 = re.compile(r'\bR-D-RD-[^P]\b')
patrones3.append(patron33)
patrones3.append(patron3)

patrones4 = []
patron4 = re.compile(r'\bD-LD-L\b')
patron44 = re.compile(r'\bD-LD-L-[^K]\b')
patrones4.append(patron44)
patrones4.append(patron4)

patrones5 = []
patron5 = re.compile(r'\bR-RD-D-LD-L\b')
patron55 = re.compile(r'\bR-RD-D-LD-L-[^K]\b')
patrones5.append(patron55)
patrones5.append(patron5)

combos.append(patrones1)
combos.append(patrones2)
combos.append(patrones3)
combos.append(patrones4)
combos.append(patrones5)






dataT = sys.argv[1]
infile = open(dataT,'r')
items = infile.readline().split()
output = open('sumbitOutput','w')

for i in range(0,int(items[0])):
	coincidencias = 0      
    case = i + 1
    golpes = infile.readline()
    print golpes
    for j in range(0, len(combos)):
		count = 0     
	    for i in range (0,len(combos[0])):
			m = patrones[j].findall(golpes)
		    count += len(m)
		 
		coincidencias += count           
    
    
    output.write("Case #"+str(case)+": "+str(count))
    print coincidencias
    output.write("\n")
infile.close()
output.close()
    
    
