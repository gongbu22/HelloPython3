# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 이름: 민지, 국어: 99, 영어: 98, 수학: 99
# 이름: 혜린, 국어: 88, 영어: 77, 수학: 66
# 이름: 다니엘, 국어: 55, 영어: 77, 수학: 99

# 성적 데이터 관련 변수 선언
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []


# 성적 데이터 입력받음
name1 = input('1번학생 이름은? ')
kor1 = int(input('1번학생 국어는? '))
eng1 = int(input('1번학생 영어는? '))
mat1 = int(input('1번학생 수학은? '))

names.append(name1)
kors.append(kor1)
engs.append(eng1)
mats.append(mat1)

name2 = input('2번학생 이름은? ')
kor2 = int(input('2번학생 국어는? '))
eng2 = int(input('2번학생 영어는? '))
mat2 = int(input('2번학생 수학은? '))

names.append(name2)
kors.append(kor2)
engs.append(eng2)
mats.append(mat2)

name3 = input('3번학생 이름은? ')
kor3 = int(input('3번학생 국어는? '))
eng3 = int(input('3번학생 영어는? '))
mat3 = int(input('3번학생 수학은? '))

names.append(name3)
kors.append(kor3)
engs.append(eng3)
mats.append(mat3)

# 성적 처리
tot = kors[0] + engs[0] + mats[0]
tots.append(tot)
avg = tots[0] / 3
grd = '수' if (avgs[0] >= 90) else \
        '우' if (avgs[0] >= 80) else \
        '미' if (avgs[0] >= 70) else \
        '양' if (avgs[0] >= 60) else '가'

avgs.append(avg)
grds.append(grd)


tot = kors[1] + engs[1] + mats[1]
tots.append(tot)
avg = tots[1] / 3
grd = '수' if (avgs[1] >= 90) else \
        '우' if (avgs[1] >= 80) else \
        '미' if (avgs[1] >= 70) else \
        '양' if (avgs[1] >= 60) else '가'
avgs.append(avg)
grds.append(grd)

tot = kors[2] + engs[2] + mats[2]
tots.append(tot)
avg = tots[2] / 3
grd = '수' if (avgs[2] >= 90) else \
        '우' if (avgs[2] >= 80) else \
        '미' if (avgs[2] >= 70) else \
        '양' if (avgs[2] >= 60) else '가'
avgs.append(avg)
grds.append(grd)


# 결과 출력
print(f'''
이름: {names[0]}, 국어: {kors[0]}, 영어: {engs[0]}, 수학: {mats[0]}
# 총점: {tots[0]}, 평균: {acg[0]:.1f}, 학점: {grds[0]}
이름: {names[1]}, 국어: {kors[1]}, 영어: {engs[1]}, 수학: {mats[1]}
# 총점: {tots[1]}, 평균: {acg[1]:.1f}, 학점: {grds[1]}
이름: {names[2]}, 국어: {kors[2]}, 영어: {engs[2]}, 수학: {mats[2]}
# 총점: {tots[2]}, 평균: {acg[2]:.1f}, 학점: {grds[2]}
''')