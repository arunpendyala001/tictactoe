n=9
tic = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
	print(tic[i])
num = []
k = 'O'
p=0
g = 1
for i in range(0,9):
	p=0
	if(k=='X'):
		k='O'
	else:
		k='X'		
	while(p==0):
		pos = int(input(k+" enter the position: "))
		if(pos>9 or pos<0):
			print("enter a position between 1 and 9")
		elif(pos in num):
			print("enter a position which is not taken!")
		else:
			if(pos==1):
				tic[0][0]=k
			elif(pos==2):
				tic[0][1]=k
			elif(pos==3):
				tic[0][2]=k
			elif(pos==4):
				tic[1][0]=k
			elif(pos==5):
				tic[1][1]=k
			elif(pos==6):
				tic[1][2]=k
			elif(pos==7):
				tic[2][0]=k
			elif(pos==8):
				tic[2][1]=k
			elif(pos==9):
				tic[2][2]=k	
			g += 1clear
			for i in range(0,3):
				print(tic[i])
			p=1
			if(tic[0][0]==k and tic[0][1]==k and tic[0][2]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[1][0]==k and tic[1][1]==k and tic[1][2]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[2][0]==k and tic[2][1]==k and tic[2][2]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[0][0]==k and tic[1][1]==k and tic[2][2]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[0][2]==k and tic[1][1]==k and tic[2][0]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[0][0]==k and tic[1][0]==k and tic[2][0]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[0][1]==k and tic[1][1]==k and tic[2][1]==k):
				print(k+" is the winner!")
				exit()
			elif(tic[0][2]==k and tic[1][2]==k and tic[2][2]==k):
				print(k+" is the winner!")
				exit()
		num.append(pos)
if(g == 10):
	print("Draw Match!")












# 00 01 02
# 10 11 12
# 20 21 22
# 00 11 22
# 02 11 20
# 00 10 20
# 01 11 21
# 02 12 22
