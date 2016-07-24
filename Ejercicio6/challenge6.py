# -*- coding: utf-8 -*-
#!/usr/bin/python


"""
USE : python challenge6.py alice_shocked.png

"""
from qrtools import QR
import Image

img = Image.open("alice_shocked_wb.png")
t= img.size
img2 = img
count = 0
for i in range(0,t[0]):
	for j in range(0,t[1]):
		color = img.getpixel((i,j))
		
		count +=1
#el 180,
		if color >= 190:
			img2.putpixel((i,j),255)
		else:
			img2.putpixel((i,j),0)
		
		
img2.save("alice_shocked5.png")


myCode =  QR(filename=u"alice_shocked5.png")

if myCode.decode():
	print myCode.data
	
