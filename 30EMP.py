# 사원 데이터기반 CRUD 기능이 제공되는 프로그램

import sys
import dangdang.emp as emp

while True:
    menu = emp.empMenu()

    if menu == '1':
        print('사원 데이터 추가')
        emp.addEmp()

    elif menu == '2':
        print('사원 데이터 조회')
        emp.showEmp()

    elif menu == '3':
        print('사원 데이터 상세조회')
        emp.showOneEmp()

    elif menu == '4':
        print('사원 데이터 수정')
        emp.modifyEmp()

    elif menu == '5':
        print('사원 데이터 삭제')
        emp.removeEmp()

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!!')