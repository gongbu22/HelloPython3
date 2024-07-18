# 변수는 맨 위에
products = {'쌀': 9900, '상추': 1900, '고추': 2900, '마늘': 8900, '통닭': 5600, '햄': 6900, '치즈': 3900}

# 단위 환산
# def readUnit():
#     length = float(input('길이(mm)를 입력하세요. '))
#     return length
#
# def convertUnit(len):
#     cm = len * 0.1
#     m = len * 0.001
#     inch = len * 0.03937
#     ft = len * 0.003281
#     return cm, m, inch, ft
#
# def printUnits(len, cm, m, inch, ft):
#     print(f'''
#     {len} mm --> {cm} cm
#     {len} mm --> {m} m
#     {len} mm --> {inch} inch
#     {len} mm --> {ft} ft
#     ''')

#---------선생님 풀이------------
def readUnit():
    mm = int(input('길이(mm)를 입력하세요. '))
    return mm

def convertUnit(mm):
    units = [mm]
    units.append(mm * 0.1)
    units.append(mm * 0.001)
    units.append(mm * 0.03937)
    units.append(mm * 0.003281)
    return units

def printUnits(units):
    print(f'''
    {units[0]} mm --> {units[1]} cm
    {units[0]} mm --> {units[2]} m
    {units[0]} mm --> {units[3]} inch
    {units[0]} mm --> {units[4]} ft
    ''')

# 할인된 상품 가격표 출력
# def readDiscount():
#     discount = int(input('오늘의 할인율을 입력하세요. '))
#     return discount
#
# def discountPrice(discount, products):
#     prices = {}
#     for k in products:
#         percent = (100-discount)*0.01
#         prices[k]=int(products[k]*percent)
#     return prices
#
# def printPrices(discount, products, disproducts):
#     for k, v in disproducts.items():
#         print(f'{k:3s} : {products[k]:5d} 원 {discount} %DC -> {v:5d} 원')
#     print(f'{"-"*40}')

#----------선생님 풀이 -------------
# products 변수는 맨 위에 있음

def readDiscount():
    print(f'''
    {"-"*40}
    -- 한빛마트 오늘의 할인 가격표 출력 시스템 --
    {"-"*40}
    ''', end='')
    rate = int(input('오늘의 할인율을 입력하세요. '))
    return rate

def printPrices(dcprice, rate):
    result = ''
    for idx, k in enumerate(products):
        result += f'{k:4s} : {products[k]:,d} 원 {rate} % DC -> {dcprice[idx]:,.0f} 원\n'
    print(result)

def discountPrice(rate):
    dcprice = []
    dc = (1 - (rate/100))
    for v in products.values():
        dcprice.append(v * dc)
    return dcprice


# 주민번호 유효성 체크
# def readJumin():
#     jumin = input('주민번호를 입력하세요. ')
#     if len(jumin) == 13:
#         if int(jumin[-7]) in (1, 2, 3, 4):
#             if int(jumin[-6:]) >= 1 and int(jumin[-6:]) <= 899999:
#                 return jumin
#
# def checkJumin(jumin):
#     mul = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
#     sum = 0
#     result = '유효하지 않습니다.'
#     for i in range(len(jumin[:12])):
#         sum += int(jumin[i]) * mul[i]
#     if int(jumin[-1]) == (11 - (sum % 11)) % 10:
#         result = '유효입니다.'
#     else:
#         result = '유효하지 않습니다.'
#     return result
#
# def printJumin(jumin, result):
#     print(f'주민번호 {jumin}은 {result}')

#--------선생님 풀이 -------------
def readJumin():
    pass

    sum = 0
    result = '유효하지 않는 주민번호입니다.'
    jumin = input('주민번호는? ')

    sum += int(jumin[0]) * 2
    sum += int(jumin[1]) * 3
    sum += int(jumin[2]) * 4
    sum += int(jumin[3]) * 5
    sum += int(jumin[4]) * 6
    sum += int(jumin[5]) * 7
    sum += int(jumin[6]) * 8
    sum += int(jumin[7]) * 9
    sum += int(jumin[8]) * 2
    sum += int(jumin[9]) * 3
    sum += int(jumin[10]) * 4
    sum += int(jumin[11]) * 5

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[12]): result = '주민번호 유효!'
    print(result)


def checkJumin(jumin):
    result = '주민번호 불일치!'
    sum = 0
    weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    for i in range(12):
        sum += int(jumin[i]) * weight[i]

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[12]): result = '주민번호 유효!'

    return result