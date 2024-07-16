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