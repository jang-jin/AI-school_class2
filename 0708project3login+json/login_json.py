import json
from getpass import getpass

path = './students.json'

# 초기 json 파일 만들기
def make_data():
    with open(path, 'w') as make_file:
        json_data = {}
        json_data['students'] = []
        json_data['promises'] = []
        json_data['interests'] = []
        json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

# json 파일 읽어오기
def load_data():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    except:
        make_data()
        return load_data()

# json 파일 저장하기
def save_data(json_data):
    with open(path, 'w', encoding='utf-8') as make_file:
        json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

# 12자 이하 아이디 비밀번호 받기
def input_12_char_below(input_type):
    if input_type == "아이디":
        input_data = input(f"{input_type} : \n")
    elif input_type == "비밀번호":
        input_data = getpass(f"{input_type} : \n")

    if len(input_data) > 12:
        print(f"{input_type}는 12자 이하로 입력해주세요!")
        return None
    elif len(input_data) <= 0:
        print(f"{input_type}를 입력해주세요!")
        return None
    else:
        return input_data.lower()

# 중복 체크 check
def duplicate_check(json_data, input_data):
    students = json_data['students']
    for student in students:
        if student['userid'] == input_data:
            print('이미 존재하는 id입니다. 다시 입력해주세요!')
            return True
    return False

# 회원가입
def join():
    json_data = load_data()

    student = {}

    try:
        student['id'] = json_data['students'][-1]['id'] + 1
    except:
        student['id'] = 1

    while True:
        student['userid'] = input_12_char_below("아이디")
        if student['userid'] is None:
            continue
        if duplicate_check(json_data, student['userid']):
            continue
        break

    while True:
        student['password'] = input_12_char_below("비밀번호")
        if not student['password']:
            continue
        break

    student['name'] = input("이름 : \n")

    while True:
        try:
            student['age'] = int(input("나이 : \n"))
            break
        except:
            print("나이는 숫자로 입력해주세요!")

    json_data['students'].append(student)

    promise = {}
    promise['id'] = student['id']
    promise['content'] = input("앞으로의 5개월 동안의 다짐 : \n")
    json_data['promises'].append(promise)

    interest = {}
    interest['id'] = student['id']
    interest['content'] = input("관심 분야 : \n")
    json_data['interests'].append(interest)

    save_data(json_data)

    print("\n회원가입이 완료되었습니다. 로그인을 해주세요.\n")

    login()

# 로그인
def login():
    json_data = load_data()

    while True:
        userid = input_12_char_below("아이디")
        if userid is None:
            continue
        break

    students = json_data['students']
    for student in students:
        if student['userid'] == userid:
            userpw = input_12_char_below("비밀번호")
            if student['password'] == userpw:
                print(f"\n{student['name']}님 환영합니다!!\n")
                service_main(student['id'])
            else:
                print("잘못된 비밀번호입니다!")
            break
        elif student['id'] == len(students):
            print("존재하지 않는 아이디입니다!")

# 마이페이지
def mypage(user_id):
    json_data = load_data()

    for student in json_data['students']:
        if student['id'] == user_id:
            print(f"아이디:{student['userid']}")
            print(f"이름:{student['name']}")
            print(f"나이:{student['age']}")
    
    for promise in json_data['promises']:
        if promise['id'] == user_id:
            print(f"앞으로 5개월 동안의 다짐:{promise['content']}")

    for interest in json_data['interests']:
        if interest['id'] == user_id:
            print(f"관심분야:{interest['content']}\n")
    
# 다른 유저 정보 보기
def anotherpage(user_id):
    json_data = load_data()

    user_ids = []
    index = 1
    for student in json_data['students']:
        if student['id'] != user_id:
            print(f"{index}. {student['name']}")
            user_ids.append(student['id'])
            index += 1

    index = int(input("자세히볼 다른 유저를 선택하세요 : \n"))
    mypage(user_ids[index-1])

# 서비스 메인
def service_main(user_id):
    while True:
        menu = input("1. 마이페이지 보기 2. 다른 유저 보기 3. 로그아웃 : \n")
        if menu == "1" :
            mypage(user_id)
        elif menu == "2" :
            anotherpage(user_id)
        elif menu == "3" :
            print("로그아웃되었습니다.")
            break
        else :
            print("잘못된 명령어입니다.\n")

def main():
    print("="*50)
    print("프로젝트3 로그인 실습 시작합니다!!")
    print("="*50)
    while True :
        menu = input("1. 회원가입 2. 로그인 3. 종료 : \n")
        if menu == "1":
            join()
        elif menu == "2":
            login()
        elif menu == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 명령어입니다.")

main()

