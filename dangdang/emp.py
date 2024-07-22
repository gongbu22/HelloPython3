import dangdang.empDAO as empdao

def empMenu():
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

def readEmp():
    empList = []
    cnt = empdao.getTotalEmp()
    empList.append(input(f'{cnt}번 사원번호는? '))
    empList.append(input(f'{cnt}번 사원의 이름은? '))
    empList.append(input(f'{cnt}번 사원의 성은? '))
    empList.append(input(f'{cnt}번 사원의 이메일은? '))
    empList.append(input(f'{cnt}번 사원의 전화번호는? '))
    empList.append(input(f'{cnt}번 사원의 입사일은? '))
    empList.append(input(f'{cnt}번 사원의 직업번호는? '))
    empList.append(input(f'{cnt}번 사원의 급여는? '))
    empList.append(input(f'{cnt}번 사원의 수당은? (없으면 0) '))
    empList.append(input(f'{cnt}번 사원의 매니저는? (없으면 0) '))
    empList.append(input(f'{cnt}번 사원의 부서번호는? (없으면 0) '))

    return empList

# 입력받은 사원 데이터를 처리하고 테이블에 저장
# 입력받은 수당, 매니저번호, 부서번호는 적절한 형변환 필요!
def addEmp():
    emp = readEmp()
    # emp[8] = float(emp[8]) if emp[8] != 0 else 'null'
    emp[8] = float(emp[8]) if emp[8] != '0' else None
    emp[9] = int(emp[9]) if emp[9] != '0' else 'null'
    emp[10] = int(emp[10]) if emp[10] != '0' else 'null'
    empdao.newEmp(emp)

def showEmp():
    result = ''
    allEmp = empdao.readAllEmp()
    for e in allEmp:
        result += f'''사원번호: {e[0]}, 이름: {e[1]}, 이메일: {e[2]}, 직책: {e[3]}, 부서번호: {e[4]}\n'''
    print(result)

def showOneEmp():
    result = '데이터가 존재하지 않습니다.'
    empid = int(input('사원번호는? '))
    oneEmp = empdao.readOneEmp(empid)

    if oneEmp:
        result = (f'사원번호: {oneEmp[0]}, 이름: {oneEmp[1]}, 성: {oneEmp[2]}, email: {oneEmp[3]} \n' 
    f'전화번호: {oneEmp[4]}, 입사일: {oneEmp[5]}, 직업번호: {oneEmp[6]}, 연봉: {oneEmp[7]} \n'
    f'상여금: {oneEmp[8]}, 매니저번호: {oneEmp[9]}, 부서번호: {oneEmp[10]}')

    print(result)

def removeEmp():
    empid = int(input('삭제할 사원번호는? '))
    result = '데이터가 존재하지 않습니다.'
    cnt = empdao.delEmp(empid)
    if cnt > 0:
        result = f'{cnt} 건의 데이터가 삭제됨!!'
    print(result)