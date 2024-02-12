#이스케이프 시퀀스 \',\",\t,\n
str1 ="\'비구름\'이 말했습니다.\n\t\"비가 내리면 먼지가 사라질거야.\""
print(str1)

#문자열 포맷팅
year=int(input())
month=int(input())
date=int(input())
day=input()
sentence1=("오늘은 {0}년 {1}월 {2}일 {3}입니다.".format(year, month, date, day))
print(sentence1)
#진짜 포멧팅은 아래의 방식이다.
sentence1=(f"오늘은 {year}년 {month}월 {date}일 {day}입니다.")
print(sentence1)
