# 1주일 내용 10문제로 끝내기

# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']

for person in people:
    if person == '장발장':
        print(f"{person} 차례 입니다, 빵을 드릴 수 없습니다.")
    else:
        print(f"{person} 차례 입니다, 빵을 하나 드리겠습니다.")

# --------------------------------------------------------

# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 없는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것

def bread(person):
    if person == '장발장':
        return 0
    else:
        return 1

for person in people:
    if bread(person):
        print(f"{person}은 빵을 먹을 수 있는 사람 입니다.")
    else:
        print(f"{person}은 빵을 먹을 수 없는 사람 입니다.")

# --------------------------------------------------------

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)


# def stamp():
#     """쿠폰 스탬프가 찍힌 횟수를 증가시키고, 화면에 출력한다."""
#     global num_stamp           # num_stamp는 전역변수다
#     num_stamp = num_stamp + 1  # 오류가 발생하지 않는다 (global 안쓰면 오류 발생함)
#     print(num_stamp)

def stamp(num_stamp):
    num_stamp += 1
    print(num_stamp)
    return num_stamp


num_stamp = stamp(num_stamp)  # 화면에 1이 출력된다
stamp(num_stamp)  # 화면에 2가 출력된다

# --------------------------------------------------------

# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것

class Transportation():
    def __init__(self, name, price, departure_time, arrival_time):
        self.name = name
        self.price = price
        self.departure_time = departure_time
        self.arrival_time = arrival_time
    def show_departure_time(self):
        print(f"출발 시간은 {self.departure_time} 입니다.")
    def show_arrival_time(self):
        print(f"도착 시간은 {self.arrival_time} 입니다.")

class Airplane(Transportation):
    def __init__(self, name, price, departure_time, arrival_time, baggage_availability):
        super().__init__(name, price, departure_time, arrival_time)
        self.baggage_availability = baggage_availability
    def leave_baggage(self):
        if self.baggage_availability:
            print("수하물을 맡겼습니다!")
        else:
            print("이 비행기는 수하물을 못맡깁니다!")

class Train(Transportation):
    def __init__(self, name, price, departure_time, arrival_time, seat_class):
        super().__init__(name, price, departure_time, arrival_time)
        self.seat_class = seat_class
    def show_seat_class(self):
        print(f"좌석 등급은 {self.seat_class} 입니다.")

airplane1 = Airplane("지니호","1000원","10시30분","12시30분",True)
airplane2 = Airplane("장지니호","10000원","15시30분","18시30분",False)
airplane1.show_arrival_time()
airplane2.show_departure_time()
airplane1.leave_baggage()
train1 = Train("지니차","300원","13시","14시","3등석") 
train2 = Train("장지니차","1500원","17시","18시","1등석") 
train1.show_arrival_time()
train2.show_departure_time()
train2.show_seat_class()
# --------------------------------------------------------

# 5. 문자열 이용하기


# 파이썬 io 하는거 2 문제
