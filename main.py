from Login import login
from facilityForUsers import facilityMain

userName = ""
userRegion = ""

def main():
    userName, userRegion = login()
    func= int(input("원하는 기능을 입력해주세요\n 1. 장학금 정보 2. 주변 청소년 복지 센터 알아보기 3. 게시판\n"))

    if func == 1:
        # 장학금 정보
        print("장학금 정보입니다.\n")
    elif func == 2:
        # 복지정보
        print("주변 청소년 복지 센터 정보입니다.\n")
        facilityMain()
    else:
        print()

    return userName, userRegion

if __name__ == "__main__":
    main()

