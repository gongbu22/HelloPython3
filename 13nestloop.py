# 중첩 반복문
# 2개 이상의 반복문을 이용해서 반복실행할 수도 있음
# 하나의 반복문 안에 다른 반복문을 포함시킨 것을 의미
# 이것을 통해 좀 더 복잡한 반복패턴을 구현할 수 있음
# 2차원 배열처리나 달력 출력, 복잡한 패턴 생성시 주로 이용

# *
# **
# ***
# ****
# *****

# 5 x 5 반복 출력
for i in range(5):      # 행
    for j in range(5):  # 열
        print('*', end='')
    print()             # 줄바꿈

# 각 반복마다 1회, 2회, 3회, 4회, 5회 출력
for i in range(1, 5+1):      # 행
    for j in range(i):  # 열
        print('*', end='')
    print()             # 줄바꿈

# *****
# ****
# ***
# **
# *

for i in range(1, 5+1):
    for j in range(5-(i-1)):
        print('*', end='')
    print()

# ------- 선생님 풀이 ----------
for i in range(5, -1):
    for j in range(i):
        print('*', end='')
    print()

# 마름모
# - 위 for문 하나
# - 아래 for문 하나
# 각 for문 안에 공백 for문, 별 for문 2개씩
# 총 4개의 for문 필요

# 구구단 출력
for i in range(1, 9+1):         # 헹/ 큰바늘
    for j in range(1, 9+1):     # 열/ 작은바늘
        print(f'{j:1d} x {i:1d} = {j * i:2d}  ', end=' ')
    print()

# 19단 출력
for i in range(1, 19+1):         # 헹/ 큰바늘
    for j in range(1, 19+1):     # 열/ 작은바늘
        print(f'{j:2d} x {i:2d} = {j * i:3d}  ', end=' ')
    print()

# 달력
# 1. 통으로 print
# 2. 행으로 먼저 print
# 3. 행/열 print
