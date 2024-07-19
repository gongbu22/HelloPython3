# 파일읽기
# with open(경로, 방식, 'r') as 파일객체변수  # 'r'은 생략가능
#   파일객체변수.read()

# 파일 기록 방식
# r (읽기)

# 파일 읽을때 사용가능한 함수
# read      : 파일의 내용을 모두 읽음
# readLine  : 파일의 내용을 한 줄씩 읽음 (반복문 필요)
# readLines : 파일의 내용을 한 줄씩 모두 읽음 (반복문 필요)

# 파일에서 간단한 인삿말 읽어오기
with open('c:/Java/hello.txt') as f:
    print(f.read())

# 파일에서 회원정보 읽어오기 1 - 단순출력
with open('c:/Java/member.dat', encoding='UTF-8') as f:
    print(f.read())

# 파일에서 회원정보 읽어오기 2 - 행단위 처리1
with open('c:/Java/member.dat', encoding='UTF-8') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

# 파일에서 회원정보 읽어오기 3 - 행단위 처리2
with open('c:/Java/member.dat', encoding='UTF-8') as f:
    while True:
        line = f.readline()     # 먼저, 한 줄 읽고
        if not line: break      # 읽은 내용이 없으면 중단
        print(line)

# 파일에서 회원정보 읽어오기 4 - 행단위 처리3  - 권장
with open('c:/Java/member.dat', encoding='UTF-8') as f:
    lines = f.readlines()   # 행단위로 읽어서 리스트에 저장

for line in lines:      # 이터러블 형식으로 반복 처리
    print(line)

# 회원정보 데이터파일에서
# 이름과 이메일만 출력
with open('c:/Java/member.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

# 문자열변수.split(구분자) : 특정문자로 문자열을 나눠 리스트에 저장
for line in lines:
    member = line.split('/')
    print(member[2], member[3], end='')

# 앞 예제에서 파일로 저장한 성적데이터를
# 다음과 같은 형태로 화면에 출력
# 이름 : abc, 국어 : 99, 영어 : 87, 수학 : 66
name = input('학생 이름은? ')
kor = input('국어 점수는? ')
eng = input('영어 점수는? ')
mat = input('수학 점수는? ')

# with open('c:/Java/sungjuk.dat', 'w', encoding='UTF-8') as f:
#     row = f'{name}, {kor}, {eng}, {mat}'
#     f.write(row)

with open('c:/Java/sungjuk.dat', 'a', encoding='UTF-8') as f:
    row = f'{name}, {kor}, {eng}, {mat}\n'
    f.write(row)

with open('c:/Java/sungjuk.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

for line in lines:
    sungjuk = line.split(',')
    row = f'이름: {sungjuk[0]}, 국어: {sungjuk[1]}, 영어: {sungjuk[2]}, 수학: {sungjuk[3]}'
    print(row, end='')
