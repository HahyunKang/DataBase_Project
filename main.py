from Login import login
import user
import facility
from facilityForUsers import facilityMain

def main():
    print("*** 소년, 소녀 가장을 위한 정보 제공 / 커뮤니티 서비스 ***\n")
    # 테이블 생성
    # user.user()
    # facility.facility()
    #---------------------------------------------------------------------------------------------------------
    userName, userRegion, userId = login()
    print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion + ", 사용자 아이디: " + str(userId) + "\n")

    func= int(input("원하는 기능을 입력해주세요\n 1. 장학금 정보 2. 주변 청소년 복지 센터 알아보기 3. 게시판\n"))

    if func == 1:
        # 장학금 정보
        print("장학금 정보입니다.\n")
    elif func == 2:
        # 복지정보
        print("주변 청소년 복지 센터 정보입니다.\n")
        facilityMain(userName, userRegion, userId)
    else:
        print()

if __name__ == "__main__":
    main()

