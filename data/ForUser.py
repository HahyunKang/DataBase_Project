from SQLCreate import SQLCreate
from connect import connect


class CreateTableForUser:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def createHighSchoolTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS HighSchoolScholarshipForUsers;")
        query = SQLCreate().createHighSchoolScholarshipForUser()
        self.cursor.execute(query)
        self.con.commit()

    def createFacilityForUser(self):
        self.cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        query = SQLCreate().createRegionToUsers()
        self.cursor.execute(query)
        self.con.commit()
        self.cursor.execute("SELECT * FROM FacilityForUsers;")
        info = self.cursor.fetchall()
        for data in info:
            print(data)

    def createUnivTable(self):
        self.cursor.execute("DROP TABLE IF EXISTS ScholarshipForUsers;")
        query = SQLCreate().createUnivScholarShipForUser()
        self.cursor.execute(query)
        self.con.commit()

    def createFacilityTable(self, userRegion):
        pass

