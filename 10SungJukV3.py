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
for i in range(0, 3):
        names.append(input(f'{i+1}번학생 이름은? '))
        kors.append(int(input(f'{i+1}번학생 국어는? ')))
        engs.append(int(input(f'{i+1}번학생 영어는? ')))
        mats.append(int(input(f'{i+1}번학생 수학은? ')))

        tots.append(kors[i] + engs[i] + mats[i])
        grd = '수' if (avgs[i] >= 90) else \
              '우' if (avgs[i] >= 80) else \
              '미' if (avgs[i] >= 70) else \
              '양' if (avgs[i] >= 60) else '가'
        avgs.append(tots[i] / 3)
        grds.append(grd)
        print(f'''
        이름: {names[i]}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {mats[i]}
        # 총점: {tots[i]}, 평균: {avgs[i]:.1f}, 학점: {grds[i]}''')


#--------선생님 풀이-------------------

names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []
# 성적 데이터 입력받음
for i in range(3):
    names.append(input(f'{i+1}번학생 이름은? '))
    kors.append(int(input(f'{i+1}번학생 국어는? ')))
    engs.append(int(input(f'{i+1}번학생 영어는? ')))
    mats.append(int(input(f'{i+1}번학생 수학은? ')))

# 성적 처리
for i in range(3):
    tot = kors[i] + engs[i] + mats[i]
    tots.append(tot)
    avg = tots[i] / 3
    avgs.append(avg)
    grd = '수' if (avgs[i] >= 90) else \
            '우' if (avgs[i] >= 80) else \
            '미' if (avgs[i] >= 70) else \
            '양' if (avgs[i] >= 60) else '가'
    grds.append(grd)

# 결과 출력
result = ''

for i in range(3):
    result += f'''
        이름: {names[i]}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {mats[i]}
    # 총점: {tots[i]}, 평균: {avgs[i]:.1f}, 학점: {grds[i]}\n'''
print(result)
