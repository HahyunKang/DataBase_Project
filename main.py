from Login import login
from SQLSelect import SQLSelect

def main():
    login()
    func= int(input("원하는 기능을 입력해주세요\n 1.장학금 정보 2. 주변 청소년복지 센터 알아보기 3.게시판\n"))

    if func == 1:
        # 장학금 정보
        print("1")
    elif func == 2:
        # 복지정보
        print("2")
        SQLSelect.selectFacilityForUsers(login)
    else:
        print()



