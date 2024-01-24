from tkinter import *
from tictoe import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")
count=1
def dicclear():
	for k,v in d.items():
		d[k]=" "
	global count
	count=1
def main(n):
	if n==2:
		dicclear()
	def click(pos,r,c):
		global count
		w=check(pos)
		if w == 1:
			if count%2==0:
				n="O"
				color="#F2F907"
			else:
				n="X"
				color="#07F9F7"
			d[pos]=n
			b=Button(text=n,font=("Bold",20),height=2,width=4,bg=color)
			b.grid(row=r,column=c)
			count=count+1	
		k=decide()
		if k=="O":
			messagebox.showinfo("information","O is winner")
			dicclear()
		elif k=="X":
			messagebox.showinfo("information","X is winner")
			dicclear()
		elif count>9:
			messagebox.showinfo("information","Game is Draw")  
			dicclear()



	
	b1=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(1,0,0))
	b1.grid(row=0,column=0)
	b2=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(2,0,1))
	b2.grid(row=0,column=1)
	b3=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(3,0,2))
	b3.grid(row=0,column=2)
	b4=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(4,1,0))
	b4.grid(row=1,column=0)
	b5=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(5,1,1))
	b5.grid(row=1,column=1)
	b6=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(6,1,2))
	b6.grid(row=1,column=2)
	b7=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(7,2,0))
	b7.grid(row=2,column=0)
	b8=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(8,2,1))
	b8.grid(row=2,column=1)
	b9=Button(text=" ",font=("Bold",20),height=2,width=4,command=lambda : click(9,2,2))
	b9.grid(row=2,column=2)
	b10=Button(text="Reset",height=1,width=12,bg="#FA7087",command=lambda:main(2))
	b10.grid(row=3,column=0,columnspan=3)
main(1)


root.mainloop()