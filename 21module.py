# 모듈
# 매우 복잡하고 긴 코드를 하나의 파일에
# 모두 작성하는 것은 비효율적일 수 있음 - 유지보수 힘듦
# 또한, 여러 사람들과 함께 개발하는 경우
# 작업분담, 작업결과물 통합 역시 어려움

# 모듈 방식의 개발을 이용하면
# 사용용도에 따라 파일별로 나눠 작성 가능
# 타인이 만들어 둔 코드를 자신의 프로그램에서 활용 가능
# 따라서, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venv/py310/Lib/site-package  - 가상환경

# 모듈 불러오기
# import 명령을 이용해서 불러올 수 있음
# 모듈 내 정의된 함수/클래스를 사용하려면
# 모듈명.함수명, 모듈명.클래스 형식으로 코드 작성
import dangdang.hello
dangdang.hello.sayHello()

from dangdang import hello
hello.sayHello()

from dangdang2 import hello2
hello2.sayHello2()

# 모듈 사용하기 1 - 모듈명,함수명
import dangdang.calc

val = dangdang.calc.add(10, 5)
print(val)

# 모듈 사용하기 2 - 함수명  - 실무에서 권장 - 메모리차지 때문
from dangdang.calc import add
from dangdang.calc import div

val = add(10, 3)
print(val)
val = div(6, 2)
print(val)

# 모듈 사용하기 3 - 함수명 - 권장X
from dangdang.calc import *

val = mul(10, 5)
print(val)
val = minus(10, 5)
print(val)

# 모듈 사용하기 4 - 별칭 - 권장
import dangdang.calc as zc

val = zc.add(10, 20)
print(val)

# 외부 모듈 사용하기
# 내장모듈이나 사용자 정의 모듈 이외에
# 다른 조직/기관이나 개인이 만든 모듈을 사용하려면
# 'pip install 모듈명' 으로  설치하면 됨
# pip install scikit-learn
# pip install pymysql  - 데이터베이스 사용할 때 필요
# pip install fastapi

# dangdang.example 에 각 문제에 대한 모듈 작성
import dangdang.example as ex

# 단위 환산 ( convertUnit / readUnit / printUnits )

# len = ex.readUnit()
# cm, m, inch, ft = ex.convertUnit(len)
# ex.printUnits(len, cm, m, inch, ft)

#-----------선생님 풀이---------
mm = ex.readUnit()
units = ex.convertUnit(mm)
ex.printUnits(units)

# 할인된 상품 가격표 출력 ( discountPrice / readDiscount / printPrices )

# print(f'''{"-"*40}
# -- 한빛마트 오늘의 할인 가격표 출력 시스템 --
# {"-"*40}''')
# discount = ex.readDiscount()
# products = {'쌀': 9900, '상추': 1900, '고추': 2900, '마늘': 8900, '통닭': 5600, '햄': 6900, '치즈': 3900}
# disProducts = ex.discountPrice(discount, products)
# ex.printPrices(discount, products, disProducts)
# ----------선생님 풀이-----------
rate = ex.readDiscount()
dcprice = ex. discountPrice(rate)
ex.printPrices(dcprice, rate)


# 주민번호 유효성 체크 ( checkJumin / readJumin / printJumin )
# 주민등록번호 앞 12 자리에
# 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5 를 곱한 값을
# 모두 더하고
# 그 결과값을 11로 나눈 나머지를 11에서 뺍니다.
# 계산 결과값이 주민등록번호 마지막 자리 숫자와 일치하면 유효!
#123456-1234567
#******-*******
#234567 892345
# 2+6+12+20+30+42+8+18+6+12+20+30
# 11 - (206 % 11) = 3 ? 7

# jumin = ex.readJumin()
# result = ex.checkJumin(jumin)
# ex.printJumin(jumin, result)

#----------선생님 풀이-----------
ex.checkJumin('1234561234567')

# ex.checkJumin('123456-1234567')