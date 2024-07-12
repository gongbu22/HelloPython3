# 4
x = 1; y = 2; z = 3
s0 = 1; v0 = 2; t = 3; g = 9.8

a = 3 * x
b = 3 * x + y
c = (x + y) / 7
d = (3 * x + y) / (z + 2)
e = s0 + v0 * t + (1/2 * g * t ** 2) # 등가속도 공식

# 5 ~ 10

# 12
#---------선생님 풀이------------------------
# 만나이 : 현재년도 - 태어난년도, 생일안지남 (-1) (민법상, 2023-06부터)
currentYear = int(input('현재년도는? '))
birthYear = int(input('생일의 년도는? '))
isPass = bool(input('생일 지남 여부는? (True/False)'))

myAge = currentYear - birthYear
# myAge = myAge if (isPass == True) else (myAge - 1)
myAge = myAge if isPass else (myAge - 1)

print(f'''현재년도가 {currentYear}이고, 
생일의 년도가 {birthYear}일 때, 
나이는 {myAge} 세 입니다.''')


# 14
seconds =int(input('몇 초인지 입력해주세요. '))
date = int(seconds / 86400)
hour = int(seconds / 3600)
min = int(seconds / 60)

print (f'{date} 일 {hour} 시간 {min} 분')

# 16 (!!)
charge = int(input('잔돈을 입력하세요. '))

fivemil =  charge // 50000
mili = (charge - (50000 * fivemil)) // 10000
fiveth = (charge - (50000 * fivemil + 10000 * mili)) // 5000
thou = (charge - (50000 * fivemil + 10000 * mili + 5000 * fiveth)) // 1000
fivehun = (charge - (50000 * fivemil + 10000 * mili + 5000 * fiveth + 1000 * thou)) // 500
hun = (charge - (50000 * fivemil + 10000 * mili + 5000 * fiveth + 1000 * thou + 500 * fivehun)) // 100
fifty = (charge - (50000 * fivemil + 10000 * mili + 5000 * fiveth + 1000 * thou + 500 * fivehun + hun * 100)) // 50
ten = (charge - (50000 * fivemil + 10000 * mili + 5000 * fiveth + 1000 * thou + 500 * fivehun + hun * 100 + fifty * 50)) // 10

print(f'''잔돈 : {charge}
5만원 : {fivemil} 개
만원 : {mili} 개
5천원 : {fiveth} 개
천원 : {thou} 개
5백원 : {fivehun} 개
백원 : {hun} 개
오십원 : {fifty} 개
십원 : {ten} 개
''')

#----------------선생님 풀이------------------------
price = 34_560
paid = 50_000
charge = paid - price

# w50000 = charge / 50000      # 결과는 float
# w50000 = int(charge / 50000) # 결과를 정수형으로 변환
w50000 = charge // 50000     # 파이썬의 몫 연산자
charge = charge % 50000

w10000 = charge // 10000
# charge = charge - (10000 * w10000)
# charge = charge % 10000
charge %= 10000

w5000 = charge // 5000
# charge = charge - (5000 * w5000)
charge %= 5000

w1000 = charge // 1000
# charge = charge - (1000 * w1000)
charge %= 1000

w500 = charge // 500
# charge = charge - (500 * w500)
charge %= 500

w100 = charge // 100
# charge = charge - (100 * w100)
charge %= 100

w50 = charge // 50
# charge = charge - (50 * w50)
charge %= 50

w10 = charge // 10
# charge = charge - (10 * w10)
charge %= 10

print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원
잔돈 : {(paid - price):,} 원
------------
50000원 : {w50000} 장
10000원 : {w10000} 장
5000원 : {w5000} 장
1000원 : {w1000} 장
500원 : {w500} 개
100원 : {w100} 개
50원 : {w50} 개
10원 : {w10} 개
''')