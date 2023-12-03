class SQLCreate:
    def __init__(self):
        self.res = None

    def createUnivScholarShipForUser(self):
        query =  "CREATE TABLE ScholarshipForUsers AS SELECT ROW_NUMBER() OVER (ORDER BY scholarshipId) AS keyId, scholarshipId, userId  FROM ScholarshipForUniv, Users WHERE univName = schoolName;"
        return query

    def createRegionToUsers(self):
        query = "CREATE TABLE FacilityForUsers AS SELECT facilityId, userId FROM WellfareFacility, Users WHERE " \
                "facilityName LIKE %s; "
        return query
        # query = f"""INSERT INTO FacilityForUsers(userId, facilityId)
        #             VALUES (
        #                 (SELECT userId FROM Users WHERE name = '{name}'),
        #                 {facility(region)}
        #             );
        #             """
        # return query

        # query = "SELECT facilityId FROM WellfareFacility WHERE address LIKE %s;"

        # return query

    def createHighSchoolScholarshipForUser(self):
        query = "CREATE TABLE HighSchoolScholarshipForUsers AS SELECT scholarshipId,userId FROM ScholarshipForHighSchool,Users WHERE (scholarType='지역연고' and institutionName LIKE %s) OR scholarType = '소득구분';"
        return query

    def createScholarShipForUser(self):
        pass
