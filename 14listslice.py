# 슬라이싱(slicing)
# 연속적인 객체들(리스트, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 시퀀스 자료형에 지원되는 기능(순서를 기억함) 중에 하나
# 객체명[시작 : 끝-1 : 스텝]

# 슬라이싱 예제
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(f'''
    {alphabet[2:6]}\n,
    {alphabet[:5]}\n,
    {alphabet[3:8]}\n,
    {alphabet[5:]}\n,
    {alphabet[3:9]}\n,
    {alphabet[:]}\n,
    {alphabet[::2]}\n,  # 2개씩 띄어서
    {alphabet[::-1]}    # 역방향
''')

# 주민번호에서 생년월일 성별코드 추출
# 문자열 슬라이스 : 문자열의 일부 추출 가능
jumin = '123456-1234567'

birth = jumin[:6]
gender = jumin[7:8]

print(birth)
print(gender)

# 33
cardno = input('카드번호는? ')

result = '잘못된 카드 번호입니다.'
if cardno[:2] == '35':
    if cardno == '356317': result = 'JCB카드 NH농협카드'
    elif cardno == '356901': result = 'JCB카드 신한카드'
    elif cardno == '356912': result = 'JCB카드 KB국민카드'
elif cardno[:1] == '4':
    if cardno == '404825': result = '비자카드 비씨카드'
    elif cardno == '438676': result = '비자카드 신한카드'
    elif cardno == '457973': result = '비자카드 국민은행'
elif cardno[:1] == '5':
    if cardno == '515594': result = '마스타카드 신한카드'
    elif cardno == '524353': result = '마스타카드 외환카드'
    elif cardno == '540926': result = '마스타카드 국민은행'
print(result)
