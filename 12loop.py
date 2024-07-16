# while 문
# 조건을 만족할 때까지 반복 수행 - 반복횟수는 모름

# 변수 = 초기값
# while 조건식:
#   반복할문장
#   변수증가/감소

# 1 ~ 10까지 정수 출력
# for i in range(1, 10+1):
#     print(i, end=' ')
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 홀수만 출력
i = 1
while i <= 50:
    print(i, end=' ')
    i += 2

i = 1
while i <= 50:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end = ' ')
    i += 1

# 반복문 내 실행 중지: break
# for, while문 내에서 반복호출을 벗어나기 위해 사용

# 1 ~ 10000사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 계산을 중지

sum = 0

for i in range(1, 10000+1):
    if sum > 12345678: break
    sum += i

print(sum, i)

sum = 0
num = 1
while sum <= 12345678:
    sum += num
    num += 1
print(sum, i)

#-----선생님 풀이--------
i = 1
sum = 0
while i < 10000+1:
    if sum > 12345678: break
    sum += i
    i += 1

print(sum, i)

# 1 ~ 100 정수 중
# 3과 8의 공배수와 최소공배수 구하기
i = 1
result = ''
while i < 101:
    if (i % 3 == 0) & (i % 8 == 0):
        result += f'{i} '
    i+=1

print(f'{result}, 최소공배수: {3*8}')

# 삼각형 너비 계산하기
i = 2
j = 3
area = 0
while i < 100:
    area = (i * j)/2
    i += 2
    j += 3
    if area > 150: break
    print(f'삼각형의 넓이: {area}, i, j')

# ----------선생님 풀이-----------
limitArea = 150 # 반복 중단 삼각형 너비
width = 2
height = 3
i = 1

while True:
    area = ((width * i) * (height * i)) / 2
    if area > limitArea: break
    print(f'삼각형의 너비 : {width * i} / {height * i} = {area}')
    i += 1


# 3 6 9 게임 (while로 작성)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)
i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == '33' or i == '66' or i == '99': jjak += ' 짝!'
    print(i, jjak)
    i += 1

# 열차 교차 시간 알아내기
trainA = 10
trainB = 25
trainC = 30

i = 1
timeHour = 0
timeMin = 0
result = ''
while i < 541:
    timeHour = 9+(i // 60)
    timeMin = i % 60
    result = f'{timeHour}시 {timeMin}분'
    if (i % trainA == 0) & (i % trainB == 0) & ( i % trainC == 0 ):
        print(result)
    elif (i % trainA == 0) & (i % trainB == 0):
        print(result)
    elif (i % trainB == 0) & ( i % trainC == 0 ):
        print(result)
    elif (i % trainA == 0) & ( i % trainC == 0 ):
        print(result)
    i += 1

# ----------선생님 풀이---------------
trainA = 10
trainB = 25
trainC = 30
min = 1

while min < 541:
    if min % trainA == 0 and min % trainB == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : A - B 교차!')
    elif min % trainB == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : B - C 교차!')
    elif min % trainA == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : A - C 교차!')
    min += 1


# 로그인 기능 만들기
passwd = input('관리자 암호를 입력하세요. ')

isLogin = False
i = 1
while i < 5:
    if not isLogin:
        passwd = input('관리자 암호를 입력하세요. ')

        if passwd == 'hanbitac':
            isLogin = True
            print('로그인 됐습니다!')
        else:
            print('암호를 다시 확인하세요!')
    i += 1
if not isLogin: print('로그인 실패! 횟수 초과!')

# ----------선생님 풀이------------
cntLogin = 1
while True:
    passwd = input('관리자 암호를 입력하세요. ')

    if passwd == 'hanbitac':
        print('로그인 되었습니다!')
        break
    else:
        print('암호를 다시 확인하세요!')

    if cntLogin < 5: cntLogin += 1
    else:
        print('로그인 실패! 횟수 초과!')
        break

