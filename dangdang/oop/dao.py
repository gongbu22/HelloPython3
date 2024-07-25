import sqlite3
import pymysql

from dangdang.oop.models import SungJuk, Employee

# 데이터베이스 연결 문자열
host = '3.39.240.55'
dbname = 'clouds2024'
user = 'clouds2024'
passwd = 'clouds2024'

# 성적 DAO 클래스
class SungJukDAO:

    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        """
        데이터베이스 연결객체외 커서 생성
        :return conn, curosr: 연결객체와 커서
        """
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        """
        데이터베이스 연결객체와 커서 종료(닫기)
        :param conn: 연결객체
        :param cursor: 커서
        """
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적 데이터를 sungjuk 테이블에 저장
        :param sj: 테이블에 저장할 성적데이터
        :return cnt: 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'insert into sungjuk(name, kor, eng, mat, tot, avg, grd) \
                values (%s,%s,%s,%s,%s,%s,%s)'

        conn, cursor = SungJukDAO._make_conn()

        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd)
        cursor.execute(sql, params)

        cnt = cursor.rowcount
        conn.commit()

        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        """
        sungjuk 테이블에서 모든 성적 데이터(번호/이름/국어/영어/수햑/등록일)를 읽어옴
        :return: 조회된 성적데이터 객체
        """
        sjs = []
        sql = 'select sjno, name, kor, eng, mat, substr(regdate, 1, 11) regdate from sungjuk;'

        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:    # 조회결과를 SungJuk 객체에 개별 저
            sj = SungJuk(r[1], r[2], r[3], r[4])
            sj.sjno = r[0]
            sj.regdate = r[5]
            sjs.append(sj)
        SungJukDAO._dis_conn(conn, cursor)

        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        """
        sungjuk 테이블에서 특정학생의 성적데이터를 읽어옴
        :param sjno: 조회할 학생의 학생번호
        :return sj: 조회된 학생의 성적데이터
        """
        sql = 'select * from sungjuk where sjno = %s'

        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()   # 하나만 가져오기

        if rs:
            sj = SungJuk(rs[1], rs[2], rs[3], rs[4])
            sj.sjno = rs[0]
            sj.tot = rs[5]
            sj.avg = rs[6]
            sj.grd = rs[7]
            sj.regdate = rs[8]
        else:
            sj = None

        SungJukDAO._dis_conn(conn, cursor)

        return sj

    @staticmethod
    def update_sungjuk(sj):
        """
        sungjuk 테이블에 성적데이터(국어, 영어, 수학, 총합, 평균, 등급 ) 수정함
        :param sj: 수정할 학생번호
        :return cnt: 테이블에 성공적으로 수정된 데이터 건수
        """
        sql = 'update sungjuk set kor=%s, eng=%s, mat=%s, tot=%s, avg=%s, grd =%s \
                where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()

        params = (sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)

        cnt = cursor.rowcount
        conn.commit()

        SungJukDAO._dis_conn(conn, cursor)

        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        """
        sungjuk 테이블에서 성적데이터 삭제함
        :param sjno: 삭제할 학생번호
        :return cnt: 테이블에 성공적으로 삭제된 데이터 건수
        """
        sql = 'delete from sungjuk where sjno = %s'
        params = (sjno, )

        conn, cursor = SungJukDAO._make_conn()

        cursor.execute(sql, params)
        conn.commit()
        cnt = cursor.rowcount

        SungJukDAO._dis_conn(conn, cursor)

        return cnt

# 사원 DAO 클래스
class EmpDAO:

    @staticmethod
    def _make_conn():
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()


    @staticmethod
    def new_emp(emp):
        sql = "insert into emp values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        conn, cursor = EmpDAO._make_conn()

        params = (emp.empid, emp.fname, emp.lname, emp.email,
                  emp.phone, emp.hdate, emp.jobid, emp.sal,
                  emp.comm, emp.mgrid, emp.deptid)

        cursor.execute(sql, params)

        cnt = cursor.rowcount
        conn.commit()

        cursor.close()
        conn.close()

        return cnt

    @staticmethod
    def select_emp():
        sql = 'select empid, fname, email, jobid, deptid from emp;'

        ala = []

        conn, cursor = EmpDAO._make_conn()

        cursor.execute(sql)
        emps = cursor.fetchall()
        for emp in emps:
            aemp = Employee(emp[0], emp[1], None, emp[2], None,
                      None, emp[3], None, None, None, emp[4])
            ala.append(aemp)

        EmpDAO._dis_conn(conn, cursor)

        return ala

    @staticmethod
    def selectone_emp(empid):
        sql = 'select * from emp where empid = %s;'

        conn, cursor = EmpDAO._make_conn()

        params = (empid, )

        cursor.execute(sql, params)
        a = cursor.fetchone()

        if a:
            emp = Employee(a[0], a[1], a[2], a[3], a[4],
                      a[5], a[6], a[7], a[8], a[9], a[10])
        else:
            emp = None

        EmpDAO._dis_conn(conn, cursor)

        return emp
    
    @staticmethod
    def update_emp(nEmp):
        sql = 'update emp set email=%s, phone=%s, jobid=%s, sal=%s, comm=%s, mgrid=%s, deptid=%s \
               where empid = %s'
        params = (nEmp.email, nEmp.phone, nEmp.jobid, nEmp.sal, nEmp.comm, nEmp.mgrid, nEmp.deptid, nEmp.empid)
    
        conn, cursor = EmpDAO._make_conn()
    
        cursor.execute(sql, params)
        conn.commit()
        cnt = cursor.rowcount
    
        EmpDAO._dis_conn(conn, cursor)

        return cnt

    @staticmethod
    def del_emp(empid):
        sql = 'delete from emp where empid = %s'
        params = (empid, )

        conn, cursor = EmpDAO._make_conn()

        cursor.execute(sql, params)
        conn.commit()

        EmpDAO._dis_conn(conn, cursor)
        cnt = cursor.rowcount

        return cnt


