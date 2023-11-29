from CommunityController import CommunityController
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
    # ---------------------------------------------------------------------------------------------------------
    while (1):
        userName, userRegion, userId = login()
        print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion + ", 사용자 아이디: " + str(userId) + "\n")
        facility.facility(userRegion)

        while (1):

            func = int(input("원하는 기능을 입력해주세요\n 1. 장학금 정보 2. 주변 청소년 복지 센터 알아보기 3. 게시판 4.로그아웃 5.종료\n"))

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
                # 복지 정보
                print("주변 청소년 복지 센터 정보입니다.\n")
                facilityInfoController = FacilityInfoController()
                facilityInfoController.getFacilityName(userId)
                query = select.selectFacilityInfo(userId)
                view.printFacilityInfo(query)

            elif func == 3:
                print("커뮤니티 정보입니다.\n")
                community = CommunityController().getCommunityName(userId)
                print(f"----{community}입니다----")
                num = input("1. 글 조회 2. 글쓰기 3. 핫게시판 보기")
                if num == 1:
                    print("글 조회")
                elif num == 2:
                    print("글 쓰기")
                else:
                    print("핫 게시판 보기")
            elif func == 4:
                print("로그아웃 되었습니다.\n")
                break
            elif func == 5:
                print("프로그램을 종료합니다.\n")
                exit()
            else:
                print("잘못 누르셨습니다. 기능을 다시 선택해주세요\n")


if __name__ == "__main__":
    main()
