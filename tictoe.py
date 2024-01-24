d={x:" " for x in range(1,10)}
def display():
	i=1
	for k,v in d.items():
		if i%3==0:
			print(v)
		else:
			print(v,end=" |")
		i=i+1
def display1():
	i=1
	for k,v in d.items():
		if i%3==0:
			print(i)
		else:
			print(i,end=" |")
		i=i+1
def check(n):
	if d[n]==" ":
		return 1
	else:
		return 0
def player1(n):
	m=check(n)
	if m==1:
		d[n]="X"
		return 1
	else:
		return 0
def player2(n):
	m=check(n)
	if m==1:
		d[n]="O"
		return 1
	else:
		return 0
def decide():
	if d[1]=="X" and d[2]=="X" and d[3]=="X":
		return "X"
	elif d[4]=="X" and d[5]=="X" and d[6]=="X":
		return "X"
	elif d[7]=="X" and d[8]=="X" and d[9]=="X":
		return "X"
	elif d[1]=="X" and d[4]=="X" and d[7]=="X":
		return "X"
	elif d[2]=="X" and d[5]=="X" and d[8]=="X":
		return "X"
	elif d[3]=="X" and d[6]=="X" and d[9]=="X":
		return "X"
	elif d[1]=="X" and d[5]=="X" and d[9]=="X":
		return "X"
	elif d[3]=="X" and d[5]=="X" and d[7]=="X":
		return "X"
	elif d[1]=="O" and d[2]=="O" and d[3]=="O":
		return "O"
	elif d[4]=="O" and d[5]=="O" and d[6]=="O":
		return "O"
	elif d[7]=="O" and d[8]=="O" and d[9]=="O":
		return "O"
	elif d[1]=="O" and d[4]=="O" and d[7]=="O":
		return "O"
	elif d[2]=="O" and d[5]=="O" and d[8]=="O":
		return "O"
	elif d[3]=="O" and d[6]=="O" and d[9]=="O":
		return "O"
	elif d[1]=="O" and d[5]=="O" and d[9]=="O":
		return "O"
	elif d[3]=="O" and d[5]=="O" and d[7]=="O":
		return "O"
if __name__=="__main__":
	count=0
	display1()
	while True:
		w=decide()
		if w=="X":
			print("X is winner")
			break
		elif w=="O":
			print("O is winner")
			break
		if count<9:
			n=int(input("player X chance [1-9]"))
			m=player1(n)
			while m==0:
				print("Already occupied ")
				n=int(input("player X chance [1-9]"))
				m=player1(n)
			display()
		else:
			break
		w=decide()
		if w=="X":
			print("X is winner")
			break
		elif w=="O":
			print("O is winner")
			break
		count=count+1
		if count<9:
			n=int(input("player O chance [1-9]"))
			m=player2(n)
			while m==0:
				print("Already occupied ")
				n=int(input("player X chance [1-9]"))
				m=player2(n)
			display()
		else:
			break
		count=count+1



