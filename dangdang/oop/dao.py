import sqlite3

from dangdang.oop.models import SungJuk


# 성적 DAO 클래스
class SungJukDAO:
    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        conn = sqlite3.connect('db/python.db')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        sql = 'insert into sungjuk(name, kor, eng, mat, tot, avg, grd) \
                values (?,?,?,?,?,?,?)'

        conn, cursor = SungJukDAO._make_conn()

        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd)
        cursor.execute(sql, params)

        cnt = cursor.rowcount
        conn.commit()

        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        sjs = []
        sql = 'select sjno, name, kor, eng, mat, substr(regdate, 0, 11) regdate from sungjuk;'

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
        sql = 'select * from sungjuk where sjno = ?'

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
        sql = 'update sungjuk set kor=?, eng=?, mat=?, tot=?, avg=?, grd =? \
                where sjno = ?'
        conn, cursor = SungJukDAO._make_conn()

        params = (sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)

        cnt = cursor.rowcount
        conn.commit()

        SungJukDAO._dis_conn(conn, cursor)

        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        sql = 'delete from sungjuk where sjno = ?'
        params = (sjno, )

        conn, cursor = SungJukDAO._make_conn()

        cursor.execute(sql, params)
        conn.commit()
        cnt = cursor.rowcount

        SungJukDAO._dis_conn(conn, cursor)

        return cnt
