from connect import connect
import webbrowser

class View:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def printUnivScholarInfo(self, query):
        print("* 대학생을 위한 장학금 혜택 *")
        print("- 지원 금액 높은 순입니다 -")
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        cnt = 0
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        cnt = 0
        for data in query:
            cnt += 1
            universityName = data[2]
            scholarName = data[3]
            scholarAmount = data[4]
            formattedAmount = "{:,.0f} 원".format(scholarAmount) # 금액 보기 쉽게 수정
            print("============================================================")
            print("학교", cnt)
            print("학교 이름: " + universityName)
            print("장학 이름: " + scholarName)
            print("지원 금액: " + formattedAmount)
        print("============================================================")


    def printFacilityInfo(self, query):
        facilityPage = []
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        cnt = 0
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        cnt = 0
        for data in query:
            cnt += 1
            facilityName = data[1]
            facilityLocation = data[3]
            facilityTelephone = data[4]
            facilityPage.append(data[5])
            pageIdx = facilityPage.index(str(data[5]))
            print("============================================================")
            print("시설", cnt)
            print("이름: " + facilityName)
            print("위치: " + facilityLocation)
            print("전화번호: " + facilityTelephone)
            print("홈페이지: " + facilityPage[pageIdx])
        print("============================================================")
        return facilityPage

    def printHighschoolScholarInfo(self, query):
        print("* 고등학생을 위한 장학금 혜택 *")
        cnt = 0
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        cnt = 0
        for data in query:
            cnt += 1
            scholarOrganization = data[1]
            scholarshipName = data[2]
            scholarshipType = data[5]
            scholarshipGrade = data[6]
            scholarshipAmount = data[7]

            print("============================================================")
            print("학교", cnt)
            print("운영 기관: " + scholarOrganization)
            print("장학 이름: " + scholarshipName)
            print("장학 종류: " + scholarshipType)
            print("대상 학년: " + scholarshipGrade)
            print("지원 금액: " + scholarshipAmount)
        print("============================================================")

    def printPostingList(self, info):
        print("* 게시판 목록 *")
        for data in info:
            postId = data[0]
            postTitle = data[1]
            postContent = data[2]
            hits = data[3]


            print("============================================================")
            print("게시판 ID: " + str(postId))
            print("게시판 제목: " + postTitle)
            print("게시판 내용: " + postContent )
            print("조회수: " + str(hits))
        print("============================================================")

    def printComments(self, info):
        print("* 댓글 목록 *")
        for data in info:
            content = data[0]
            userId = data[1]

            print("---------------------------------------------------------")
            print("유저 아이디: " + str(userId))
            print("댓글: " + content)

        print("---------------------------------------------------------")

    def printApplicationUniv(self, info):
            print("* 신청 목록 *")
            cnt = 0
            for data in info:
                cnt += 1
            cnt = 0
            for data in info:
                cnt += 1
                universityName = data[2]
                scholarName = data[3]
                scholarAmount = data[4]
                formattedAmount = "{:,.0f} 원".format(scholarAmount)  # 금액 보기 쉽게 수정
                print("============================================================")
                print("학교", cnt)
                print("학교 이름: " + universityName)
                print("장학 이름: " + scholarName)
                print("지원 금액: " + formattedAmount)
            print("============================================================")

    def printApplicationHighschool(self, info):
        print("* 신청목록 *")
        cnt = 0
        for data in info:
            cnt += 1
        cnt = 0
        for data in info:
            cnt += 1
            scholarOrganization = data[1]
            scholarshipName = data[2]
            scholarshipType = data[5]
            scholarshipGrade = data[6]
            scholarshipAmount = data[7]

            print("============================================================")
            print("학교", cnt)
            print("운영 기관: " + scholarOrganization)
            print("장학 이름: " + scholarshipName)
            print("장학 종류: " + scholarshipType)
            print("대상 학년: " + scholarshipGrade)
            print("지원 금액: " + scholarshipAmount)
        print("============================================================")
