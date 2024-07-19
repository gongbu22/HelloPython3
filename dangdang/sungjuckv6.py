def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
==========================
    성적 프로그램 v6
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

# 성적 데이터 관련 변수 선언
sjs = []

# 성적데이터를 입력 받는 함수
def readSungJuck():
    sjList = []
    cnt = len(sjs)
    sjList.append(input(f'{cnt}번학생 이름은? '))
    sjList.append(int(input(f'{cnt}번학생 국어는? ')))
    sjList.append(int(input(f'{cnt}번학생 영어는? ')))
    sjList.append(int(input(f'{cnt}번학생 수학은? ')))

    return sjList

def addSungJuck(sjList):
    sjList.append(sjList[1] + sjList[2] + sjList[3])
    sjList.append(sjList[4] / 3)
    grd = '수' if (sjList[5] >= 90) else \
        '우' if (sjList[5] >= 80) else \
            '미' if (sjList[5] >= 70) else \
                '양' if (sjList[5] >= 60) else '가'
    sjList.append(grd)
    # 입력받은 성적 데이터를 리스트에 저장
    sjs.append(sjList)



# 리스트에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}\n'
        print(result)


# sungjuk.dat에 저장된 성적데이터를 읽어서
# sjs 변수에 초기화
def loadSungJuk():
    with open('dangdang/sungjuk.dat', 'r', encoding='UTF-8') as f:
        rows = f.readlines()

    for row in rows:
        sj = []
        data = row.split(',')
        sj = [ d for d in data ]
        sjs.append(sj)

    # # sjs에 변수값 넣기
    # sjList = []
    # cnt = len(sjs)+1
    # sjList.append(input(f'{cnt}번학생 이름은? '))
    # sjList.append(int(input(f'{cnt}번학생 국어는? ')))
    # sjList.append(int(input(f'{cnt}번학생 영어는? ')))
    # sjList.append(int(input(f'{cnt}번학생 수학은? ')))
    # sjList.append(sjs[1] + sjs[2] + sjs[3])
    # sjList.append(sjs[4] / 3)
    # grd = '수' if (sjs[5] >= 90) else \
    #     '우' if (sjs[5] >= 80) else \
    #     '미' if (sjs[5] >= 70) else \
    #     '양' if (sjs[5] >= 60) else '가'
    # sjList.append(grd)
    # return


# 메모리에 생성된 sjs변수의 모든 성적데이터를
# sungjuk.dat에 저장
def saveSungJuk(sjs):
    with open('dangdang/sungjuk.dat', 'a', encoding='UTF-8') as f:
        sungjuk = f'{sjs[0]}, {sjs[1]}, {sjs[2]}, {sjs[3]}, {sjs[4]}, {sjs[5]}\n'
        f.write(sungjuk)

# 데이터 초기화 함수 호출
loadSungJuk()