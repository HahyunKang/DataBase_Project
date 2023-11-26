from SQLSelect import SQLSelect
from connect import connect


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
    for i in query:
        print(i)
    selectName = SQLSelect().selectUserName(username) # 사용자 이름 뽑아오기
    cursor.execute(selectName)
    query2 = cursor.fetchall()
    for i in query2:
        print(i)
    for rowName in query2:
        print("[ 로그인 ] " + rowName[0] + " 님 환영합니다!\n")

    # 지역 떼어오기
    selectRegion = SQLSelect().selectUserRegion(username)
    cursor.execute(selectRegion)
    query2 = cursor.fetchall()
    for rowRegion in query2:
        print(rowRegion[0])
    
    return (rowName[0], rowRegion[0])
if __name__ == "__main__":
    login()
