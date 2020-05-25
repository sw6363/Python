while True:
    number = int(input('2 이상의 정수를 입력하세요 (종료: -1): '))
    if number == -1:
        break
    count = 2
    is_prime = True
    while count < number:
        if number % count == 0:
            is_prime = False
            break
        count = count+1
    if is_prime:
        print('소수입니다')
    else:
        print('소수가 아닙니다')
