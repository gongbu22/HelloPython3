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


# 입력받은 성적 데이터를 테이블에 저장
def addSungJuk(sjList):
    computeSungJuk(sjList)
    newSungJuck(sjList)


# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    sjs = readAllSungJuk()
    for sj in sjs:
        result += f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]}, 등록일: {sj[5]}\n'
    print(result)

# 학생 이름으로 성적데이터 조회 후 출력
def showOneSungJuk():
    # name = input('학생 이름은?')
    sjno = input('조회할 학생 번호는?')
    result = '데이터가 존재하지 않습니다.'
    sj = readOneSungJuk(sjno)
    if sj:  # 조회한 데이터가 존재한다면
        result = (f'번호: {sj[0]}, 이름: {sj[1]}, 국어: {sj[2]}, 영어: {sj[3]}, 수학: {sj[4]} \n'
                f'총점: {sj[5]}, 평균: {sj[6]}, 학점: {sj[7]}, 등록일: {sj[8]}\n')
    print(result)

#------------------------------------

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

# 처리된 성적데이터를 테이블에 저장
def newSungJuck(sjList):
    sql = 'insert into sungjuk(name, kor, eng, mat, tot, avg, grd) \
            values (?,?,?,?,?,?,?)'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    params = (sjList[0], sjList[1], sjList[2], sjList[3], sjList[4], sjList[5], sjList[6])
    cursor.execute(sql, params)

    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()

    cursor.close()
    conn.close()

def readAllSungJuk():
    sql = 'select sjno, name, kor, eng, mat, substr(regdate, 0, 11) regdate from sungjuk;'

    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql)
    sjs = cursor.fetchall()

    cursor.close()
    conn.close()

    return sjs

# 학생 한명의 성적 상세 조회
def readOneSungJuk(sjno):
    sql = 'select * from sungjuk where sjno = ?'
    # sql = 'select * from sungjuk where name = :name'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    # params = {'name': name}
    params = (sjno,)
    cursor.execute(sql, params)
    sj = cursor.fetchone()   # 하나만 가져오기
    cursor.close()
    conn.close()
    return sj