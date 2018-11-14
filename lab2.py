import tkinter as tk
from tkinter import simpledialog
a = [1,2,3,4,5]
def list_repeat(a):
		b = [a[0],a[4]]
		return(b)
print (a)
a = list_repeat(a)
print (a)
c=[1,13,24,16,23,46,78,96,45,10,12]
def list_5(c):
	d = [c[0],c[1],c[2],c[3],c[4]]
	return (d)
c = list_5(c)
print (c)
e =[1,2,3,4,5,6,7,8,9,89,98]
def list_sr(e):
		f = c[0:5]
		return (f)
e = list_sr (e)
print (e)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c=[]
for num in (a):
		if num in b:
				c.append(num)
print (c)
a=[3,6,8,2,5,8,4]
b =[3,13,2,4,5,8,5]
c=[]
for num in (a):
		if num in (b):
				c.append(num)
print (c)
answer = simpledialog.askstring("Input", "Yu numbers!", parent=tk.Tk())