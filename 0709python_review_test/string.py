# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

path = "D:/Python/AI-school/0709python_review_test/swit_chat.json"

with open(path, 'r', encoding='utf-8') as jsonfile:
    swit_chat_data = json.load(jsonfile)

    # 유저별 글 쓴 횟수
    users_content = {}
    for user in swit_chat_data['data']:
        if user['content'] is not None:
            if users_content.get(user['user_name']):
                users_content[user['user_name']] += 1
            else:
                users_content[user['user_name']] = 1

    print(users_content)

    # 가장 많이 채팅한 사람 찾기
    max_count = 0
    for user in users_content.keys():
        if users_content[user] > max_count:
            max_count = users_content[user]
            max_user_content = user
        elif users_content[user] == max_count:
            max_user_content += ", "+user

    print(max_user_content)
    

# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기