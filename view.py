from DataBase_Project.connect import connect

class View:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def printUnivScholarInfo(self, query):
        print("* 대학생을 위한 장학금 혜택 *")
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        cnt = 0
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        for data in query:
            universityName = data[2]
            scholarName = data[3]
            scholarAmount = data[4]
            formattedAmount = "{:,.0f} 원".format(scholarAmount) # 금액 보기 쉽게 수정
            print("============================================================")
            print("학교 이름: " + universityName)
            print("장학 이름: " + scholarName)
            print("지원 금액: " + formattedAmount)
        print("============================================================")

    def printFacilityInfo(self, query):
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        cnt = 0
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        for data in query:
            facilityName = data[1]
            facilityLocation = data[3]
            facilityTelephone = data[4]
            facilityPage = data[5]
            print("============================================================")
            print("이름: " + facilityName)
            print("위치: " + facilityLocation)
            print("전화번호: " + facilityTelephone)
            print("홈페이지: " + facilityPage)
        print("============================================================")

    def printHighschoolScholarInfo(self, query):
        print("* 고등학생을 위한 장학금 혜택 *")
        cnt = 0
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        for data in query:
            cnt += 1
        print("당신을 위한 혜택이 " + str(cnt) + "건 존재합니다.")
        for data in query:
            scholarOrganization = data[1]
            scholarshipName = data[2]
            scholarshipType = data[5]
            scholarshipGrade = data[6]
            scholarshipAmount = data[7]

            print("============================================================")
            print("운영 기관: " + scholarOrganization)
            print("장학 이름: " + scholarshipName)
            print("장학 종류: " + scholarshipType)
            print("대상 학년: " + scholarshipGrade)
            print("지원 금액: " + scholarshipAmount)
        print("============================================================")
