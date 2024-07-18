# 성적 데이터 관련 변수 선언
sjs = [ ['일지매', 99, 87, 65, 251, 63.7, '우'] ]

def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
==========================
    성적 프로그램 v5
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

