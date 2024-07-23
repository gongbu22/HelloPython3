# 사원 데이터기반 CRUD 기능이 제공되는 프로그램
# 사원 - empid, fname, lname, email, phone,
#       hdate, jobid, sal, comm, mgrid, deptid
# 조회 - 사원번호, 이름, 이메일, 직책, 부서번호
# 상세조회 - 특정 사원번호 대상 모든 컬럼 출력

import sqlite3

def getTotalEmp():
    sql = 'select count(empid) empid from emp'
    cnt = 0
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql)
    empTotal = cursor.fetchone()
    cnt = empTotal[0]

    cursor.close()
    conn.close()

    return cnt

def newEmp(empList):
    sql = "insert into emp values (?,?,?,?,?,?,?,?,?,NULLIF(?,'NULL'),NULLIF(?,'NULL'))"
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    params = (empList[0], empList[1], empList[2], empList[3],
              empList[4], empList[5], empList[6], empList[7],
              empList[8], empList[9], empList[10])

    cursor.execute(sql, params)

    print(cursor.rowcount, '건의 데이터가 추가되었습니다.')
    conn.commit()

    cursor.close()
    conn.close()

def readAllEmp():
    sql = 'select empid, fname, email, jobid, deptid from emp;'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql)
    allEmp = cursor.fetchall()

    cursor.close()
    conn.close()

    return allEmp

def readOneEmp(empid):
    sql = 'select * from emp where empid = ?;'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    params = (empid, )

    cursor.execute(sql, params)
    oneEmp = cursor.fetchone()

    cursor.close()
    conn.close()

    return oneEmp

def delEmp(empid):
    sql = 'delete from emp where empid = ?'
    params = (empid, )

    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql, params)
    conn.commit()

    cursor.close()
    conn.close()

    cnt = cursor.rowcount

    return cnt

def updateEmp(nEmp):
    sql = ('update emp set email=?, phone=?, jobid=?, sal=?, comm=?, mgrid=?, deptid=? \
           where empid = ?')
    params = (nEmp[1], nEmp[2], nEmp[3], nEmp[4], nEmp[5], nEmp[6], nEmp[7], nEmp[8])

    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()

    cursor.execute(sql, params)
    conn.commit()
    print(cursor.rowcount, '건의 데이터 수정됨!')

    cursor.close()
    conn.close()