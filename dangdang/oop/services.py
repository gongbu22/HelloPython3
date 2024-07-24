from dangdang.oop.models import SungJuk, Employee
from dangdang.oop.dao import SungJukDAO as sjdao, EmpDAO as empdao

# 성적 서비스 클래스
class SungJukService:
    # 데코레이터 : 함수에 추가기능을 구현할때 사용
    @staticmethod  # 정적static 메서드 : 객체화없이 바로 사용가능한 메서드
                    # 정적메서드로 정의된 함수는 self 매개변수 지정 x
                    # 호출방법 : 클래스명.함수명
    def display_menu():
        """
        성적프로그램의 기능이 담긴 메뉴를 작성함
        :return menu: 선택한 메뉴번호
        """
        main_menu = '''
        ==========================
            성적 프로그램 v8
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

    @staticmethod
    def read_sungjuk():
        """
        sungjuk 테이블에 저장할 성젝데이터 입력받기
        :return SungJuk(name,kor,eng,mat) : 입력받은 성적데이터(이름,국어,영어,수학)
        """
        name = input(f'새로운 학생 이름은? ')
        kor = int(input(f'새로운 학생 국어는? '))
        eng = int(input(f'새로운 학생 영어는? '))
        mat = int(input(f'새로운 학생 수학은? '))
        return SungJuk(name, kor, eng, mat)

    @staticmethod
    def add_sungjuk():
        """
        sungjuk 테이블에 성적데이터 추가
        :return result : 추가성공 메시지
        """
        sj = SungJukService.read_sungjuk()
        SungJukService.compute_sungjuk(sj)
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt} 건의 데이터 추가 성공!!'
        print(result)

    @staticmethod
    def compute_sungjuk(sj):
        """
        입력받은 성적데이터(국어,영어,수학)로 총점,평균,등급 계산해서 Sungjuk에 넣기
        :param sj: 성적데이터(이름,국어,영어,수학)
        """
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90) : sj.grd = '수'
        elif (sj.avg >= 80) : sj.grd = '우'
        elif (sj.avg >= 70) : sj.grd = '미'
        elif (sj.avg >= 60) : sj.grd = '양'

    @staticmethod
    def show_sungjuk():
        """
        성적데이터(번호,이름,국어,영어,수학,등록일) 조회함
        :return result: 성적데이터(번호,이름,국어,영어,수학,등록일) 출력메시지
        """
        sjs = sjdao.select_sungjuk()
        result = ''
        for sj in sjs:
            result += f'번호: {sj.sjno}, 이름: {sj.name}, 국어: {sj.kor},'\
                    f'영어: {sj.eng}, 수학: {sj.mat}, 등록일: {sj.regdate}\n'
        print(result)

    @staticmethod
    def showone_sungjuk():
        """
        조회할 학생번호를 입력받고 조회결과를 출력함
        :return result: 해당 학생의 모든 데이터 출력메시지
        """
        sjno = input('조회할 학생 번호는?')
        result = '데이터가 존재하지 않습니다.'
        sj = sjdao.selectone_sungjuk(sjno)
        if sj:  # 조회한 데이터가 존재한다면
            result = (f'번호: {sj.sjno}, 이름: {sj.name}, 국어: {sj.kor}, 영어: {sj.eng}, 수학: {sj.mat} \n'
                      f'총점: {sj.tot}, 평균: {sj.avg}, 학점: {sj.grd}, 등록일: {sj.regdate}\n')
        print(result)

    @staticmethod
    def modify_sungjuk():
        """
        수정할 학생번호를 입력받고 수정결과를 출력함
        :return result: 수정완료 메시지
        """
        sjno = int(input('수정할 학생 번호는? '))
        sj = sjdao.selectone_sungjuk(sjno)
        result = '수정할 데이터가 존재하지 않습니다.'

        if sj:  # 수정할 데이터가 존재한다면
            sj = SungJukService.readAgain_sungjuk(sj)
            cnt = sjdao.update_sungjuk(sj)
            result = f'{cnt}건의 데이터 수정되었습니다.'

        print(result)

    @staticmethod
    def readAgain_sungjuk(sj):
        """
        수정할 데이터를 입력받음
        :param sj: 수정할 학생번호의 기존 데이터
        :return nsj: 수정할 새로운 데이터
        """

        # sj.kor = int(input(f'{sj.name} 학생의 새로운 국어는? ({sj.kor}) '))
        # sj.eng = int(input(f'{sj.name} 학생의 새로운 영어는? ({sj.eng}) '))
        # sj.mat = int(input(f'{sj.name} 학생의 새로운 수학은? ({sj.mat}) '))
        #
        # SungJukService.compute_sungjuk(sj)
        # return sj

        nsj = SungJuk(sj.name, None, None, None)
        nsj.kor = int(input(f'{sj.name} 학생의 새로운 국어는? ({sj.kor}) '))
        nsj.eng = int(input(f'{sj.name} 학생의 새로운 영어는? ({sj.eng}) '))
        nsj.mat = int(input(f'{sj.name} 학생의 새로운 수학은? ({sj.mat}) '))
        SungJukService.compute_sungjuk(nsj)
        nsj.sjno = sj.sjno # nsj[7] - 학생번호
        return nsj

    @staticmethod
    def remove_sungjuk():
        """
        삭제할 학생 번호를 입력받고 삭제성공메시지를 출력함
        """
        sjno = int(input('삭제할 학생 번호는? '))
        cnt = sjdao.delete_sungjuk(sjno)
        print(f'{cnt}건의 데이터가 삭제되었습니다.')

# 사원 서비스 클래스
class EmpService:
    @staticmethod
    def emp_menu():
        main_menu = '''
    ==========================
         사원 프로그램 v7b
    ==========================
        1. 사원 데이터 추가
        2. 사원 데이터 조회
        3. 사원 데이터 상세조회
        4. 사원 데이터 수정
        5. 사원 데이터 삭제
        0. 사원 데이터 종료
    ==========================  
    '''
        print(main_menu, end='')
        menu = input('=> 메뉴를 선택하세요: ')
        return menu

    @staticmethod
    def read_emp():
        # cnt = empdao.getTotalEmp()
        empid = int(input(f'새로운 사원번호는? '))
        fname = input(f'새로운 사원의 이름은? ')
        lname = input(f'새로운 사원의 성은? ')
        email = input(f'새로운 사원의 이메일은? ')
        phone = input(f'새로운 사원의 전화번호는? ')
        hdate = input(f'새로운 사원의 입사일은? ')
        jobid = input(f'새로운 사원의 직업번호는? ')
        sal = int(input(f'새로운 사원의 급여는? '))
        comm = float(input(f'새로운 사원의 수당은? (없으면 0) '))
        mgrid = int(input(f'새로운 사원의 매니저는? (없으면 0) '))
        deptid = int(input(f'새로운 사원의 부서번호는? (없으면 0) '))

        return Employee(empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)


    @staticmethod
    def add_emp():
        emp = EmpService.read_emp()
        # emp[8] = float(emp[8]) if emp[8] != 0 else 'null'
        emp.comm = emp.comm if emp.comm != 0.00 else None
        emp.mgrid = emp.mgrid if emp.mgrid != 0 else None
        emp.deptid = emp.deptid if emp.deptid != 0 else None
        cnt = empdao.new_emp(emp)

        print(f'{cnt} 건이 추가되었습니다.')


    @staticmethod
    def show_emp():
        result = ''
        allemp = empdao.readall_emp()
        for e in allemp:
            result += f'''사원번호: {e.empid}, 이름: {e.fname}, 이메일: {e.email}, 직책: {e.jobid}, 부서번호: {e.deptid}\n'''
        print(result)

    @staticmethod
    def showone_emp():
        result = '데이터가 존재하지 않습니다.'
        empid = int(input('사원번호는? '))
        oneEmp = empdao.readone_emp(empid)

        if oneEmp:
            result = (f'사원번호: {oneEmp.empid}, 이름: {oneEmp.fname}, 성: {oneEmp.lname}, email: {oneEmp.email} \n'
                      f'전화번호: {oneEmp.phone}, 입사일: {oneEmp.hdate}, 직업번호: {oneEmp.jobid}, 연봉: {oneEmp.sal} \n'
                      f'상여금: {oneEmp.comm}, 매니저번호: {oneEmp.mgrid}, 부서번호: {oneEmp.deptid}')

        print(result)

    @staticmethod
    def readagain_emp(oneEmp):
        nEmp = Employee(oneEmp.empid, oneEmp.fname, oneEmp.lname, oneEmp.email, oneEmp.phone,
                        oneEmp.jobid, oneEmp.hdate, oneEmp.sal, oneEmp.comm, oneEmp.mgrid, oneEmp.deptid)
        nEmp.email = input(f'{oneEmp.fname} 사원의 이메일은? ({oneEmp.email}) ')
        nEmp.phone = input(f'{oneEmp.fname} 사원의 전화번호는? ({oneEmp.phone}) ')
        nEmp.jobid = input(f'{oneEmp.fname} 사원의 직책은? ({oneEmp.jobid}) ')
        nEmp.sal = int(input(f'{oneEmp.fname} 사원의 급여는? ({oneEmp.sal}) '))
        nEmp.comm = float(input(f'{oneEmp.fname} 사원의 수당은? ({oneEmp.comm}) (없으면 0) '))
        nEmp.mgrid = int(input(f'{oneEmp.fname} 사원의 상사번호는? ({oneEmp.mgrid}) (없으면 0) '))
        nEmp.deptid = int(input(f'{oneEmp.fname} 사원의 부서번호는? ({oneEmp.deptid}) (없으면 0) '))
        nEmp.comm = float(nEmp.comm) if nEmp.comm != '0' else None
        nEmp.mgrid = int(nEmp.mgrid) if nEmp.mgrid != '0' else 'null'
        nEmp.deptid = int(nEmp.deptid) if nEmp.deptid != '0' else 'null'
        return nEmp

    @staticmethod
    def modify_emp():
        empid = int(input('수정할 사원번호는? '))
        oneEmp = empdao.readone_emp(empid)
        if oneEmp:
            oneEmp = EmpService.readagain_emp(oneEmp)
            cnt = empdao.update_emp(oneEmp)
            print(f'{cnt}건이 수정되었습니다.')
        else:
            print('수정할 데이터가 존재하지 않습니다.')


    @staticmethod
    def remove_emp():
        empid = int(input('삭제할 사원번호는? '))
        result = '데이터가 존재하지 않습니다.'
        cnt = empdao.del_emp(empid)
        if cnt > 0:
            result = f'{cnt} 건의 데이터가 삭제됨!!'
        print(result)
