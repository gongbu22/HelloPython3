import sqlite3

def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
==========================
    성적 프로그램 v7
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
    cnt = getTotalSungJuk()
    sjList.append(input(f'{cnt}번학생 이름은? '))
    sjList.append(int(input(f'{cnt}번학생 국어는? ')))
    sjList.append(int(input(f'{cnt}번학생 영어는? ')))
    sjList.append(int(input(f'{cnt}번학생 수학은? ')))

    return sjList

# 성적 데이터 총 갯수 조회
def getTotalSungJuk():
    sql = 'select count(sjno) total from sungjuk;'
    cnt = 0
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    for r in rs:
        cnt = r[0] + 1

    cursor.close()
    conn.close()

    return cnt


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

# 입력받은 성적 데이터를 테이블에 저장
def addSungJuk(sjList):
    computeSungJuk(sjList)

    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    sql = 'insert into sungjuk values (?,?,?,?,?,?,?)'
    params = (sjList[0], sjList[1], sjList[2], sjList[3], sjList[4], sjList[5], sjList[6])

    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터가 추가됨')
    conn.commit()

    cursor.close()
    conn.close()


# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    sql = 'select * from sungjuk;'
    cursor.execute(sql)
    rs = cursor.fetchall()

    result = ''
    sjs = readAllSungJuk()
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 총점: {sj[4]}, 평균: {sj[5]}, 등급: {sj[6]}\n'
    print(result)

    cursor.close()
    conn.close()


# 처리된 성적데이터를 테이블에 저장
def newSungJuck(sjList):
    pass

def readAllSungJuk():
    pass