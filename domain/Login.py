from SQLSelect import SQLSelect
from connect import connect

userName = ""
userRegion = ""
userId = 0

def login():
    con = connect()
    cursor = con.cursor()
    print("로그인하기\n")
    username = input("이름을 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")

    n = SQLSelect().correctId(username, password)
    cursor.execute(n)
    query = cursor.fetchall()
    for i in query:
        correctName = i[0]

    pwd = SQLSelect().correctPasssword(password)
    cursor.execute(pwd)
    query = cursor.fetchall()
    for i in query:
        correctPassword = i[0]
    # print(correctName, correctPassword)
    
    ################ 로그인 ############################
    # 로그인 예외 처리 - 제대로 안 돼서 각주처리 해놓음
    # 동명이인 처리가 안 됨;;
    if (int(correctName) != int(correctPassword) or int(correctPassword) < 0 or int(correctPassword) > 100):
        # 이름과 비밀번호 불일치 시
        while (int(correctName) != int(correctPassword)):
            print("비밀번호가 틀렸습니다. 다시 입력하세요.\n")
            password = input("비밀번호를 입력하세요 : ")
            pwd = SQLSelect().correctPasssword(password)
            cursor.execute(pwd)
            query = cursor.fetchall()
            for i in query:
                correctPassword = i[0]

    # 로그인 -> 사용자 정보 얻어오기
    select = SQLSelect().selectUser(username, password)
    cursor.execute(select)
    query = cursor.fetchall()
    for rowId in query:
        id = rowId[0]
        print(rowId)
    selectName = SQLSelect().selectUserName(username) # 사용자 이름 뽑아오기
    cursor.execute(selectName)
    query2 = cursor.fetchall()
    for rowName in query2:
        name = rowName[0]
        print("[ 로그인 ] " + name + " 님 환영합니다!\n")

    # 지역 떼어오기
    selectRegion = SQLSelect().selectUserRegion(username, password)
    cursor.execute(selectRegion)
    query2 = cursor.fetchall()
    for rowRegion in query2:
        region = rowRegion[0]

    return (name, region, id)

# if __name__ == "__main__":
#     userName, userRegion = login()
#     print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion)