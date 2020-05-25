for num in range(3):
    print('안녕 거북이', num)

num=0
while num<3:
    print('안녕 거북이', num)
    num=num+1

count=0
while count<5:
    count=count+1
    print(count, '번째 바퀴입니다')
print('경주 끝!')

name=input('이름이 뭔가요?')
print(name, '안녕!')

answer=''
while answer != '런던':
    answer=input('영국의 수도는 어디일까요?')
print('정답입니다')

count=0
while count<3:
    count=count+1
    if count == 2:
        continue
    print(count)
 
count=0
while count<3:
    count=count+1
    if count == 2:
        break
    print(count)

