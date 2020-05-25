for count in range(1, 3):
    if count==2:
        break
    print(count)

while True:
    answer = input('런던, 파리, 서울 중 영국의 수도는 어디일까요?')
    if answer == '런던':
        print('정답입니다. 런던은 영국의 수도입니다.')
        break
    elif answer == '파리':
        print('파리는 프랑스의 수도입니다.')
    elif answer == '서울':
        print('서울은 대한민국의 수도입니다.')
    else:
        print('보기에서 골라주세요')
