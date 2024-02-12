def investing(a,b):
	#순이익 임의 변수 설정
	profit = a
	
	for i in range(1,b+1):
		c = int(input(f"{i}일차 변동 데이터를 입력하세요: "))
		a = a + a*c/100
		result = a-profit # 순이익
		
	return int(result)

a = int(input("투자 액수를 입력하세요: "))
b = int(input("투자한 날짜 수를 입력하세요: "))

answer = investing(a,b)
print(answer)

if answer>0:
	print("이득입니다.")
	
elif answer==0:
	print("본전입니다.")

elif answer<0:
	print("손해입니다.")
