from SQLSelect import SQLSelect
from connect import connect

userName = ""
userRegion = ""
userId = 0

def login():
    print("로그인하기\n")
    username = input("이름을 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    con = connect()
    cursor = con.cursor()

    # 로그인 -> 사용자 정보 얻어오기
    ################ TODO 로그인 예외 처리 ############################
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
    selectRegion = SQLSelect().selectUserRegion(username)
    cursor.execute(selectRegion)
    query2 = cursor.fetchall()
    for rowRegion in query2:
        region = rowRegion[0]
    
    return (name, region, id)
        
# if __name__ == "__main__":
#     userName, userRegion = login()
#     print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion)