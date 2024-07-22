import sqlite3

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

def delSungJuk(sjno):
    sql = 'delete from sungjuk where sjno = ?'
    params = (sjno, )

    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, '건의 데이터가 삭제됨!')

    cursor.close()
    conn.close()