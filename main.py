from domain.Login import login
from data import facility
from SQL.SQLSelect import SQLSelect
from SchoolInfoController import SchoolInfoController
from data.facilityForUsers import facilityMain
from view.view import View


def main():

    view = View()
    select = SQLSelect()
    print("*** 소년, 소녀 가장을 위한 정보 제공 / 커뮤니티 서비스 ***\n")
    #---------------------------------------------------------------------------------------------------------
    userName, userRegion, userId = login()
    print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion + ", 사용자 아이디: " + str(userId) + "\n")
    facility.facility(userRegion)

    func= int(input("원하는 기능을 입력해주세요\n 1. 장학금 정보 2. 주변 청소년 복지 센터 알아보기 3. 게시판\n"))

    if func == 1:
        # 장학금 정보
        print("장학금 정보입니다.\n")
        schoolInfoController = SchoolInfoController()
        schoolName = schoolInfoController.getSchoolName(userId)
        if schoolName.__contains__("대학교"):
            query = select.selectUnivScholashipInfo(userId)
            view.printUnivScholarInfo(query)

    elif func == 2:
        # 복지정보
        print("주변 청소년 복지 센터 정보입니다.\n")
        facility.facility(userRegion)
        facilityMain(userName, userRegion, userId)
    else:
        print()

if __name__ == "__main__":
    main()

