from CommunityController import CommunityController
from SQLCreate import SQLCreate
from SQLSelect import SQLSelect
from ScholarshipController import ScholarshipController
from data import facility
from data.ForUser import CreateTableForUser
from domain.Login import login
from SchoolInfoController import SchoolInfoController
from FacilityInfoController import FacilityInfoController
from view import View
import webbrowser


def main():
    global data
    view = View()
    select = SQLSelect()
    forUser = CreateTableForUser()
    schoolInfoController = SchoolInfoController()
    forUser.createHighSchoolTable()
    forUser.createFacilityForUser()
    forUser.createUnivTable()

    print("*** 소년, 소녀 가장을 위한 정보 제공 / 커뮤니티 서비스 ***\n")
    # ---------------------------------------------------------------------------------------------------------
    while 1:
        userName, userRegion, userId = login()
        print("사용자 이름: " + userName + ", 사용자 지역: " + userRegion + ", 사용자 아이디: " + str(userId) + "\n")
        data = None

        while 1:
            func = int(input("원하는 기능을 입력해주세요\n 1. 장학금 정보 2. 주변 청소년 복지 센터 알아보기 3. 게시판 4.로그아웃 5.종료\n"))

            if func == 1:
                # 장학금 정보
                s = True
                print("장학금 정보입니다.\n")
                schoolName = schoolInfoController.getSchoolName(userId)
                print(schoolName)
                if schoolName.__contains__("대학교"):
                    query = select.selectUnivScholashipInfo(userId)
                    view.printUnivScholarInfo(query)
                    data = ScholarshipController().getUnivScholarship(userId)
                    num = input("신청하고 싶은 장학금이 있으면 번호를 입력해주세요. 없다면 Q을 눌러주세요.")
                    while s:
                        if num.upper() == 'Q':
                            s = False
                        else:
                            id = data[int(num) - 1][0]
                            ScholarshipController().apply(userId, id)
                            print("신청완료 되었습니다.")
                            data = ScholarshipController().getUnivApplication(userId)
                            view.printApplicationUniv(data)
                            s= False
                else:
                    print("원하는 장학 종류를 선택하세요\n1. 소득구분 2. 지역연고 3. 전체보기")
                    num = int(input())
                    if num == 1:
                        query = select.selectHighSchoolScholashipInfoSoduek(userId)
                        view.printHighschoolScholarInfo(query)
                    elif num == 2:
                        query = select.selectHighSchoolScholashipInfojiyeok(userId)
                        view.printHighschoolScholarInfo(query)
                    elif num == 3:
                        query = select.selectHighSchoolScholashipInfo(userId)
                        view.printHighschoolScholarInfo(query)
                        data = ScholarshipController().getHighSchoolScholarship(userId)
                        num = input("신청하고 싶은 장학금이 있으면 번호를 입력해주세요. 없다면 Q을 눌러주세요.")
                        while s:
                            if num.upper() == 'Q':
                                s = False
                            else:
                                id = data[int(num) - 1][0]
                                ScholarshipController().apply(userId, id)
                                print("신청완료 되었습니다.")
                                data = ScholarshipController().getHighSchoolApplication(userId)
                                view.printApplicationHighschool(data)
                                s = False


            elif func == 2:
                # 복지 정보
                print("주변 청소년 복지 센터 정보입니다.\n")
                query = select.selectFacilityInfo(userId)
                facilityPage = view.printFacilityInfo(query)
                pageCnt = len(facilityPage)
                print("둘러보고 싶은 홈페이지가 있으신가요? 번호를 입력하세요. (보고 싶은 홈페이지가 없으면 Q를 눌러주세요)")
                num = input()
                while 1:
                    if num.upper() == 'Q':
                        break
                    if (int(num) < 1 or int(num) > pageCnt):
                        print("없는 페이지입니다.")
                    else:
                        webbrowser.open(facilityPage[int(num) - 1])
                        break

            elif func == 3:
                print("커뮤니티 정보입니다.\n")
                community = CommunityController().getCommunityName(userId)
                print(f"* {community}입니다 *\n")
                num = int(input("1. 글 조회 2. 글쓰기\n"))
                if num == 1:
                    print("글 조회\n")
                    view.printPostingList(CommunityController().getPostings(userId))
                    postId = int(input("조회할 글 ID를 입력해주세요!: "))
                    CommunityController().viewPost(postId)
                    view.printPostingList(CommunityController().getSelectedPost(postId))
                    comments = CommunityController().viewComments(postId)
                    view.printComments(comments)

                    option = int(input("1. 댓글 쓰기 2. 나가기\n"))
                    if option == 1:
                        comment = input("내용: ")
                        CommunityController().commentings(postId, userId, comment)
                        view.printComments(CommunityController().getCommentings(postId))
                    elif option == 2:
                        continue
                elif num == 2:
                    print("글 쓰기\n")
                    title = input("제목: ")
                    content = input("내용: \n")
                    CommunityController().postings(userId, title, content)
                    view.printPostingList(CommunityController().getPostings(userId))



            elif func == 4:
                print("[로그아웃] 로그아웃 되었습니다.\n")
                break
            elif func == 5:
                print("프로그램을 종료합니다.\n")
                exit()
            else:
                print("잘못 누르셨습니다. 기능을 다시 선택해주세요\n")


if __name__ == "__main__":
    main()
