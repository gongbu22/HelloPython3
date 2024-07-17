# 성적 처리 프로그램 v4
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 리스트 형태로 저장

import sys

# 프로그램 메뉴 정의
main_menu = '''
==========================
    성적 프로그램 v4
==========================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 성적 데이터 종료
==========================
'''

# 성적 데이터 관련 변수 선언
sjs = [ ['일지매', 99, 87, 65, 251, 63.7, '우'] ]

# 메뉴 출력 및 메뉴별 처리

for sj in sjs:
    # 프로그램 주 실행부
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요: ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sjList = []
        cnt = len(sj)
        sjList.append(input(f'{cnt}번학생 이름은? '))
        sjList.append(int(input(f'{cnt}번학생 국어는? ')))
        sjList.append(int(input(f'{cnt}번학생 영어는? ')))
        sjList.append(int(input(f'{cnt}번학생 수학은? ')))

        sjList.append(sjList[1] + sjList[2] + sjList[3])
        sjList.append(sjList[4] / 3)
        grd = '수' if (sjList[5] >= 90) else \
            '우' if (sjList[5] >= 80) else \
            '미' if (sjList[5] >= 70) else \
            '양' if (sjList[5] >= 60) else '가'
        sjList.append(grd)
        # 입력받은 성적 데이터를 리스트에 저장
        sjs.append(sjList)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f'''
                이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}
                총점: {sj[4]}, 평균: {sj[5]}, 등급: {sj[6]}''')

    elif menu == '3':
        print('성적 데이터 상세조회')
        pass
    elif menu == '4':
        print('성적 데이터 수정')
        pass
    elif menu == '5':
        print('성적 데이터 삭제')
        pass
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!!')