# TODO_0 : csv 모듈 불러오기
import sqlite3

path = "D:/Python/AI-school/0709project4login+csv+sqlite/students.db"

def create_db():
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    sql = """create table students (
        id text,
        pw text
    )"""
    cur.execute(sql)
    conn.close()

def insert_db(id, pw):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    sql = "insert into students values (?, ?)"
    cur.execute(sql, (id, pw))
    conn.commit()
    conn.close()

def select_all_db():
    all_db = []
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    sql = "select * from students"
    cur.execute(sql)
    for row in cur:
        all_db.append([row[0], row[1]])
    conn.close()
    return all_db

def user_input():
    try:
        id, pw = map(str, input("아이디와 비밀번호를 차례로 입력해주세요 : ").split())
        return id, pw
    except:
        print("올바르지 않은 입력입니다!")
        id, pw = user_input()
        return id, pw

# TODO_1 : signin 함수를 구현해서 로그인 시키기
# 1. csv 파일에서 존재하는 아이디인지 확인하기
# 2. 존재하면 비밀번호 맞는지 체크
# 3. 비밀번호도 맞으면 로그인성공 출력하기

def signin(id, pw):
    students_db = select_all_db()
    exist = False
    for student in students_db:
        if student[0] == id:
            exist = True
            if student[1] == pw:
                print("로그인 성공!!")
            else:
                print("비밀번호가 틀렸습니다!")
    if not exist:
        print("존재하지 않는 아이디입니다.")

# TODO_2 : csvfile 에 유저가 존재하는지 확인하는 함수 구현해서 호출하기
# 1. 아이디를 기준으로 존재하는 유저인지 확인
# 2. 존재한다면 다시 아이디를 입력받고,
# 3. 존재하지 않는다면 다음 단계로 넘겨주기

def check_exist_id():
    while True:
        students_db = select_all_db()
        id = input("아이디 : \n")
        exist = False
        for student in students_db:
            if student[0] == id:
                exist = True
        if exist:
            print("이미 존재하는 아이디입니다.")
            continue
        else:
            return id

# TODO_3 : csvfile 에 등록되어있는 형태로 유저 등록하는 함수 구현하기
# 1. 아이디와 비밀번호를 그냥 데이터로 받아서 추가해보기
# 2. 아이디와 비밀번호를 '딕셔너리' 형태로 받아서 추가해보기 (프로그래밍 실력의 기본은 구글링! 최대한 구글링 해보세요!!)

def signup(id, pw):
    insert_db(id, pw)

def userlist():
    print("현재 존재하는 유저 :")

    # TODO_4 : csvfile 에서 현재 가입되어 있는 유저 전부 출력하기

    students_db = select_all_db()
    for student in students_db:
        print(student[0])

def exitcheck():
    stop = int(input("\n계속하시려면 0, 종료하시려면 1을 눌러주세요. : "))
    if stop == 0:
        start()
    elif stop == 1:
        exit()


def start():
    print('sqlite 로 데이터 다루기 로그인 예제')

    signup_or_login = input('1 - 로그인 / 2 - 회원가입 : \n')

    if signup_or_login == "1":
        id, pw = user_input()
        # TODO_5 : 위의 TODO1 참고 후 signin 함수 실행하기
        signin(id, pw)
    elif signup_or_login == "2":
      # TODO_6 : 회원가입을 아이디와 비밀번호만 받아서 진행할 것
      # 1. 존재하는지 확인 (위의 TODO_2의 함수 활용)
      # 2. 문제 없으면 회원가입 완료 후 userlist() 함수 구현
        id = check_exist_id()
        pw = input("비밀번호 : \n")

        signup(id, pw)
        userlist()
    else:
        print("올바른 숫자를 입력하세요!")

    exitcheck()

#create_db()
start()

# TODO_7 : 깃헙에 업로드하고 깃헙 주소 제출!
