from DataBase_Project.SQLSelect import SQLSelect
from DataBase_Project.connect import connect

userName = ""
userRegion = ""
userId = 0

def login():
    con = connect()
    cursor = con.cursor()
    print("[로그인]\n")
    username = input("이름을 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")

    correctLogin = -1

    n = SQLSelect().correctId(username, password)
    cursor.execute(n)
    query = cursor.fetchall()
    for i in query:
        correctLogin = i[0]

    if (correctLogin == -1):
        while (correctLogin == -1):
            print("비밀번호가 틀렸습니다. 다시 입력하세요.\n")
            password = input("비밀번호를 입력하세요 : ")
            n = SQLSelect().correctId(username, password)
            cursor.execute(n)
            query = cursor.fetchall()
            for i in query:
                correctLogin = i[0]

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