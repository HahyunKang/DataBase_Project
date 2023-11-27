from SQLCreate import SQLCreate
from SQLSelect import SQLSelect
from data import facility
from data.ForUser import CreateTableForUser
from domain.Login import login
from SchoolInfoController import SchoolInfoController
from FacilityInfoController import FacilityInfoController
from view import View


def main():

    view = View()
    select = SQLSelect()
    forUser = CreateTableForUser()
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
        else:
            forUser.createHighSchoolTable(userRegion)
            query = select.selectHighSchoolScholashipInfo(userId)
            view.printHighschoolScholarInfo(query)


    elif func == 2:
        # 복지정보
        print("주변 청소년 복지 센터 정보입니다.\n")
        facilityInfoController = FacilityInfoController()
        facilityInfoController.getFacilityName(userId)
        query = select.selectFacilityInfo(userId)
        view.printFacilityInfo(query)


    else:
        print()

if __name__ == "__main__":
    main()

