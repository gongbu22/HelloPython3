# 51 구구단
result = '''
         Multiplication Table
       1  2  3  4  5  6  7  8  9
---------------------------------
'''
for i in range(1, 10):
    result += f'{i:3d} | '
    for j in range(1, 10):
        result += f'{i * j:2d} '
    result += '\n'
print(result)

# -------- 선생님 풀이-----------------
print('''
         Multiplication Table
      1   2   3   4   5   6   7   8   9
-----------------------------------------
''', end='')
for i in range( 1, 9+1):
    print(f'{i} |', end='')
    for j in range(1, 9+1):
        print(f'{i * j:4d}', end = '')
    print()


# 51 달력
inputYear = int(input('연도를 입력하세요. '))

day = int((((inputYear-1)*365 + (inputYear-1)/4 - (inputYear-1)/100 + (inputYear-1)/400) % 7 ) + 1)
blank = 0
result = '''
            January 2005
-----------------------------------
 Sun  Mon  Tue  Wed  Thu  Fri  Sat
'''
for i in range(10):
    result += f'{" "* (7-blank) + 1}'
    for j in range(32):
        pass
    print(result)

# 16 계산하기 - 리스트, 반복문, 함수
price = 34_560
paid = 50_000
charge = paid - price

moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
wonCnt = []
for i in range(len(moneys)):
    if (charge // moneys[i]) == 0:
        wonCnt.append(0)
    else:
        wonCnt.append(charge // moneys[i])
    charge %= moneys[i]
print(wonCnt)

print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원
잔돈 : {charge:,} 원
------------
50000원 : {wonCnt[0]} 장
10000원 : {wonCnt[1]} 장
5000원 : {wonCnt[2]} 장
1000원 : {wonCnt[3]} 장
500원 : {wonCnt[4]} 개
100원 : {wonCnt[5]} 개
50원 : {wonCnt[6]} 개
10원 : {wonCnt[7]} 개
''')



def compute_charge(price, paid):
    charge = paid - price

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    wonCnt = []
    for i in range(len(moneys)):
        if (charge // moneys[i]) == 0:
            wonCnt.append(0)
        else:
            wonCnt.append(charge // moneys[i])
        charge %= moneys[i]
    print(wonCnt)

    print(f'''
    금액 : {price:,} 원
    지불금액 : {paid:,} 원
    잔돈 : {charge:,} 원
    ------------
    50000원 : {wonCnt[0]} 장
    10000원 : {wonCnt[1]} 장
    5000원 : {wonCnt[2]} 장
    1000원 : {wonCnt[3]} 장
    500원 : {wonCnt[4]} 개
    100원 : {wonCnt[5]} 개
    50원 : {wonCnt[6]} 개
    10원 : {wonCnt[7]} 개
    ''')

compute_charge(34560, 50000)

# ----------- 선생님 풀이 ------------
price = 34_560
paid = 50_000

def compute_charge(price, paid):
    charge = paid - price

    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    charges = []
    for money in moneys:
        charges.append(charge // money)
        charge %= money
    result = f'''
    금액 : {price:,} 원
    지불금액 : {paid:,} 원
    잔돈 : {charge:,} 원
    ------------
    '''
    for idx, m in enumerate(moneys):
        result += f'{m}원 : {charges[idx]} 장/개\n\t'

    print(result)

# 잔돈 구하는 함수 호출 및 테스트
price = int(input('지불해야 할 금액은? '))
paid = int(input('받은 금액은? '))

compute_charge(price, paid)
