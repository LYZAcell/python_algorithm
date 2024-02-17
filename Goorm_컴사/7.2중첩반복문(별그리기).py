'''a = 공백
b = 별 개수
a +b = x
별 표시'''

x =  int(input())

for i in range (1,x+1):
	print(" "*(x-i)+"*"*i)
	i+1






'''#이전 코드
x = int(input())

for i in range(1,x+1) :
	for j in range (x-i):
		print(' ',end='')
	
	for k in range (i):
		print('*',end='')

	print('')
	
	
for i in range(10,0,-1):
	print(i)
	
'''
