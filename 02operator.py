# 수식/표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자
# 자료형 승격promotion

# 한줄씩 출력 Ctrl + Shift + e

# 매출액 입력시 총합 출력
jan = int(input('1월 매출 : '))
feb = int(input('2월 매출 : '))
mar = int(input('3월 매출 : '))
total = jan + feb + mar
print(f'''1월 매출 : {jan}
2월 매출 : {feb}
3월 매출 : {mar}
1분기 전체 매출 : {total} 원
''')

# 1분기 수익 계산
sales = int(input('1분기 매출 : '))
purchase = int(input('1분기 매입 : '))
profit = sales - purchase

print(f'''1분기 매출 : {sales}
1분기 매입 : {purchase}
수익 : {profit} 원 
''')

# 방의 넓이 구하기
width = int(input('가로 길이 : '))
height = int(input('세로 길이 : '))
area = width * height

print(f'''가로 길이 : {width}
세로 길이 : {height}
넓이 : {area} ㎠
''')

# 신체질량지수BMI 구하기
weight = 87
height = 1.88
BMI = int(weight/(height**2))

print(f'''몸무게(kg) : {weight}
신장(m) : {height}
BMI : {BMI}
''')

# 홀짝 게임
coin = input('손 안에 동전 수를 입력하세요. ')
game = int(coin) % 2

print(game)

# 빵 나누기
bread = 97
students = int(input('빵을 나누어 줄 수 있는 학생 수 '))
rest = 97 % (students*3)

print(f'남은 빵 개수: {rest}')

# 점염병 예상 감염자 구하기
print('30일 이후 예상 감염자 수 : ', 2**30)

# 할당 연산자
# 변수에 값을 대입하는 데 사용하는 연산자, 대입 연산자
# ex) =, +=, -=, *=, ...

# 논리 연산자
# 피연산자의 논리 자료형(True/False)를 이용하는 연산자, and, or, not
# not -> and -> or 순서

# 논리 연산자 단축식 평가
# and 연산자 - 한쪽이 false일 경우 더 평가하지 않고 바로 false 반환
# or 연산자 - 한쪽이 true일 경우 더 평가하지 않고 바로 true 반환

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 참일때값 if 조건식 else 거짓일때값

myScore = 95
result = '합격!' if myScore >= 90 else '불합격!'

print(result)

# 복리 계산기
# 복리 계산 = 원금 * ( 1 + 이자율 ) 기간 제곱
money = 5000000
total = int(money * (1.05**5))
print(f'5년 후 총 수령액 : {total} 원')

#--------선생님 풀이--------------
money = 5_000_000
rate = 0.05
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액
money = money + (money * rate)  # 1년후 총 금액

print(f'5년 후 총 수령액 : {int(money):,} 원')

# 범퍼카 탑승
height = float(input('어린이의 신장을 입력하세요. '))
boarding = 'True' if height >= 120 else 'False'
print(boarding)

#--------선생님 풀이--------------
child = int(input('어린이의 신장을 입력하세요 : '))
isRide = (child >= 120)

# 범퍼카 탑승 가능 판별
childHeight = float(input('어린이의 신장을 입력하세요. '))
childBoarding = 'True' if childHeight >= 120 and childHeight < 170 else 'False'
print(childBoarding)

#-------선생님 풀이--------------
child = int(input('어린이의 신장을 입력하세요 : '))
isRide = (child >= 120) & (child < 170)

print(f'{isRide}')

# 적자/흑자 판별
income = int(input('수입이 얼마입니까? '))
spend = int(input('지출이 얼마입니까? '))

moneyResult = '흑자' if income > spend else '적자'
print(moneyResult)

