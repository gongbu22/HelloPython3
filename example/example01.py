# 실전예제 1 - 비밀번호 메일 발송
name = '홍길동'
email = 'gildong@abc.com'
id = 'gildong'
pw = '1234'

# print(f'To. {email}')
# print(f'▶ {name} 고객님 안녕하세요.')
# print(f'  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다.')
# print(f'  아이디 :  {id}')
# print(f'  비밀번호 :  {pw}')

print(f'''To. {email}
▶ {name} 고객님 안녕하세요.
  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다.
  아이디 :  {id}
  비밀번호 :  {pw}''')

# 실전예제 2 - 날씨 예보 프로그램
# day = '월'
# date = '3월 30일'
# minTemp = -1
# maxTemp = 10
# rainy = 45
# dusty = '좋음'
# riseSun = '오전 6시 30분'
# downSun = '오후 7시 20분'
# southWave = 0.5
# eastWave = 1.5
# westWave = 0.5

day = input('요일은? ')
date = input('날짜(월일)는? ')
minTemp = input('최저 기온은? ')
maxTemp = input('최고 기온은? ')
rainy = input('비올확률은? ')
dusty = input('미세먼지는? ')
riseSun = input('일출시간은? ')
downSun = input('일몰시간은? ')
southWave = input('남해 물결높이는? ')
eastWave = input('동해 물결높이는? ')
westWave = input('서해 물결높이는? ')

print(f'''내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보됐습니다.
비올 확률은 {rainy}%이고, 미세먼지는 {dusty} 수준일 것으로 예상됩니다.
일출 시간은 {riseSun}이고, 일몰 시간은 {downSun}입니다.
바다의 물결은 남해 앞바다 {southWave}m, 동해 앞바다 {eastWave}m, 서해 앞바다 {westWave}m 높이로 일겠습니다.
지금까지 {date} {day}요일 날씨 예보였습니다.
''')

# 영수증 예제
soju = 3000
chicken = 12000
money = int(input('받은 금액이 얼마입니까? '))
today = '2014. 07. 07. 14:35:24'

print(f'''[ 음식나라 ]
-----------------------
소주     2    {soju*2}
너나치킨  1    {chicken}
-----------------------
과세합계       {int((soju*2+chicken)*0.9)}
부가세         {int((soju*2+chicken)*0.1)}
------------------------
총합계         {soju*2+chicken}
받은금액        {money}
잔돈           {money - (soju*2+chicken)}
-------------------------
{today}
''')

#---------------
date = '2014. 07. 07. 14:35:24'
soju = 2
chicken = 1

total = (soju * 3000) + (chicken * 12000)
vat = int(total * (10/110))  # 부가세 = 합계금액 * 10/110
supply = int(total * (100/110)) # 공급가액 = 합계급액 * 100/110
paid = 50000
charge = paid - total

print(f'''[ 음식나라 ]
-----------------------
소주\t\t{soju}\t\t{soju*3000}
너나치킨\t{chicken}\t\t{chicken*12000}
-----------------------
과세합계\t{supply}
부가세\t{vat}
------------------------
총합계\t\t\t{total}
받은금액\t\t\t{paid}
잔돈\t\t\t\t{charge}
-------------------------
{date}
''')



# 11
name = '홍길동'
weight = 40
age = 25

name = input('이름이 무엇입니까? ')
weight = input('몸무게가 몇 kg 입니까? ')
age = input('나이가 몇 입니까? ')

print(name, weight, age)

# 12 - 생년월일 계산
# 연나이 계산 : 현재년도 - 태어난 년도 (병역법, 교육법, 민방위)
# 만나이 계산 : 현재년도 - 태어난 년도, 생일안지남 (-1) (민법상, 2023년 6월부터)
# 한국식 나이 : 현재년도 - 태어난 년도 + 1
birthYear = int(input('태어난 년도가 언제입니까? '))
todayYear = 2024
myage = todayYear-birthYear+1
print(f'{myage}세 입니다.')


# 13
num = int(input('몇단 입니까?'))

print(f'''[ {num}단 ]
{num} x 1 = {num*1}
{num} x 2 = {num*2}
{num} x 3 = {num*3}
{num} x 4 = {num*4}
{num} x 5 = {num*5}
{num} x 6 = {num*6}
{num} x 7 = {num*7}
{num} x 8 = {num*8}
{num} x 9 = {num*9}
''')
