class SQLCreate:
    def __init__(self):
        self.res = None

    def createScholarShipForUser(self):
        query = "CREATE TABLE ScholarshipForUsers AS SELECT scholarshipId, userId FROM ScholarshipForUniv, Users WHERE univName = schoolName;"
        return query

    def createRegionToUsers(self):
        query = "CREATE TABLE FacilityForUsers AS SELECT facilityId, userId FROM WellfareFacility, Users WHERE facilityName LIKE %s;"
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