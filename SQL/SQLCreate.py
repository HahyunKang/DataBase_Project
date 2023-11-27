class SQLCreate:
    def __init__(self):
        self.res = None

    def createScholarShipForUser(self):
        query = "CREATE TABLE ScholarshipForUsers AS SELECT scholarshipId, userId FROM ScholarshipForUniv, Users WHERE univName = schoolName;"
        return query