from data.facility import facility


class SQLSelect:
    def __init__(self):
        self.res = None

    # 로그인을 위한 함수 ------------------------------------------------------------------------
    def selectUser(self, username, password):
        query = f"SELECT * FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query

    def selectUserName(self, username):
        query = f"SELECT name FROM Users WHERE name = '{username}'"
        return query

    def selectUserRegion(self, username):
        query = f"SELECT region FROM Users WHERE name = '{username}'"
        return query

    def correctId(self, username, password):
        query = f"SELECT userId FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query

    def correctPasssword(self, password):
        query = f"SELECT userId FROM Users WHERE password = '{password}'"
        return query

    # ------------------------------------------------------------------------------------------------

    # 사회 복지 시설을 위한 함수 ----------------------------------------------------------------------
    # def insertRegionToUsers(self, userName, region):
    #     query = f"""INSERT INTO FacilityForUsers
    #                 SELECT facilityId, userId
    #                 FROM WellfareFacility, Users
    #                 WHERE address like '%{region}%' AND name = '{userName}';
    #             """
    #     return query

    def insertRegionToUsers(self, name, region):
        regionQuery = facility(region)
        for i in regionQuery:
            print(i)
        # query = f"""INSERT INTO FacilityForUsers(userId, facilityId)
        #             VALUES (
        #                 (SELECT userId FROM Users WHERE name = '{name}'),
        #                 {facility(region)}
        #             );
        #             """
        # return query

        # query = "SELECT facilityId FROM WellfareFacility WHERE address LIKE %s;"

        # return query

    def selectRegionToUsers(self, id):
        # query = f"""SELECT *
        #             FROM  WellfareFacility
        #             WHERE facilityId IN (
        #                 SELECT facilityId
        #                 FROM FacilityForUsers
        #                 WHERE userId = '{id}'
        #             )
        #             """
        query = f"SELECT * FROM FacilityForUsers"
        return query

    def selectUniv(self, univName):
        query = f"SELECT * FROM Users WHERE univName = '{univName}'"
        return query

    def selectUserRegion(self, username, password):
        query = f"SELECT region FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query

    def selectFacilityForUsers(self, region):
        query = f"SELECT * FROM WellfareFacility WHERE address like '%{region}%'"
        return query

    # -------
    def selectFacility(self, userId):
        query = f"SELECT region FROM Users WHERE userId= {userId}"
        return query

    def selectFacilityInfo(self, userId):
        query = f"SELECT * FROM WellfareFacility WHERE facilityId IN (SELECT facilityId FROM FacilityForUsers WHERE userId = {userId})"
        return query

    # -------------------------------------------------------------------------------------------------
    def selectSchool(self, userId):
        query = f"SELECT schoolName FROM Users WHERE userId= {userId}"
        return query

    def selectUnivScholashipInfo(self, userId):
        query = f"SELECT * FROM ScholarshipForUniv WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"ScholarshipForUsers WHERE userId = {userId}) ORDER BY supportAmount DESC"
        return query

    def selectHighSchoolScholashipInfo(self, userId):
        query = f"SELECT * FROM ScholarshipForHighSchool WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"HighSchoolScholarshipForUsers WHERE userId = {userId}) "
        return query

    def selectHighSchoolScholashipInfoSoduek(self, userId):
        query = f"SELECT * FROM ScholarshipForHighSchool WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"HighSchoolScholarshipForUsers WHERE userId = {userId} AND scholarType = '소득구분') "
        return query

    def selectHighSchoolScholashipInfojiyeok(self, userId):
        query = f"SELECT * FROM ScholarshipForHighSchool WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"HighSchoolScholarshipForUsers WHERE userId = {userId} AND scholarType = '지역연고') "
        return query
    # -------------------------------------------------------------------------------------------------
    def selectCommunity(self, userId):
        query = f"SELECT communityName FROM Community WHERE userId = {userId}"
        return query

    def selectCommunityId(self, userId):
        query = f"SELECT communityId FROM Community WHERE userId = {userId}"
        return query

    def selectPostings(self, communityId):
        query = f"SELECT postId,title,content,hits FROM Post WHERE regionId = {communityId}"
        return query

    def selectComments(self, postId):
        query = f"SELECT content, writerId FROM Comment WHERE postId = {postId}"
        return query

    def selectApplicationForUniv(self, userId):
        query = f"SELECT * FROM ScholarshipForUniv WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"application WHERE userId = {userId})"
        return query

    def selectApplicationForHighSchool(self, userId):
        query = f"SELECT * FROM ScholarshipForHighSchool WHERE scholarshipId IN (SELECT scholarshipId FROM " \
                f"application WHERE userId = {userId}) "
        return query
    def selectPostId(self, communityId):
        query = f"SELECT postId FROM Post WHERE regionId = {communityId}"
        return query

    def selectPost(self,postId):
        query = f"SELECT postId,title,content,hits FROM Post WHERE postId = {postId}"
        return query
