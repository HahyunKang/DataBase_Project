from SQLSelect import SQLSelect
from connect import connect


def login():
    print("로그인하기\n")
    username = input("이름을 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    con = connect()
    cursor = con.cursor()
    select = SQLSelect().selectUser(username, password)
    print(select)
    cursor.execute(select)
    query = cursor.fetchall()
    for i in query:
        print(i)


if __name__ == "__main__":
    login()
