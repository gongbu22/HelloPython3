import dangdang.sungjukv7bDAO as sjv7dao

def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
==========================
    성적 프로그램 v7b
==========================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 성적 데이터 종료
==========================
'''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')
    return menu

def readSungJuk():
    sjList = []
    cnt = sjv7dao.getTotalSungJuk()
    sjList.append(input(f'{cnt}번학생 이름은? '))
    sjList.append(int(input(f'{cnt}번학생 국어는? ')))
    sjList.append(int(input(f'{cnt}번학생 영어는? ')))
    sjList.append(int(input(f'{cnt}번학생 수학은? ')))

    return sjList


# 입력받은 성적 데이터를 테이블에 저장
def addSungJuk(sjList):
    computeSungJuk(sjList)
    sjv7dao.newSungJuck(sjList)


# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    sjs = sjv7dao.readAllSungJuk()
    for sj in sjs:
        result += f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}, 등록일: {sj[5]}\n'
    print(result)

# 학생 이름으로 성적데이터 조회 후 출력
def showOneSungJuk():
    # name = input('학생 이름은?')
    sjno = input('조회할 학생 번호는?')
    result = '데이터가 존재하지 않습니다.'
    sj = sjv7dao.readOneSungJuk(sjno)
    if sj:  # 조회한 데이터가 존재한다면
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]} \n'
                f'총점: {sj[5]}, 평균: {sj[6]}, 학점: {sj[7]}, 등록일: {sj[8]}\n')
    print(result)

# 입력한 성적데이터에 대해 성적처리하는 함수
def computeSungJuk(sjList):
    sjList.append(sjList[1] + sjList[2] + sjList[3])
    sjList.append(round(sjList[4] / 3, 2))
    grd = '수' if (sjList[5] >= 90) else \
        '우' if (sjList[5] >= 80) else \
        '미' if (sjList[5] >= 70) else \
        '양' if (sjList[5] >= 60) else '가'
    sjList.append(grd)
    return sjList

# 학생번호를 입력받아 데이터 삭제
def deleteSungJuk():
    sjno = int(input('삭제할 학생 번호는? '))
    sjv7dao.delSungJuk(sjno)

# 학생번호를 입력받아 데이터 수정
def modifySungJuk():
    sjno = int(input('수정할 학생 번호는? '))
    sjList = sjv7dao.readOneSungJuk(sjno)
    if sjList:  # 수정할 데이터가 존재한다면
        sjList = readAgainSungJuk(sjList)
        sjv7dao.updateSungJuk(sjList)
    else:
        print('수정할 데이터가 존재하지 않습니다.')

# 기존 성적 데이터를 확인하면서 수정할 성적데이터 재입력
def readAgainSungJuk(sjList):
    nsj = []
    nsj.append(sjList[1])   # nsj[0] - 학생이름
    nsj.append(int(input(f'{sjList[1]} 학생의 새로운 국어는? ({sjList[2]}) ')))
    nsj.append(int(input(f'{sjList[1]} 학생의 새로운 영어는? ({sjList[3]}) ')))
    nsj.append(int(input(f'{sjList[1]} 학생의 새로운 수학은? ({sjList[4]}) ')))
    computeSungJuk(nsj)
    nsj.append(sjList[0]) # nsj[7] - 학생번호
    return nsj