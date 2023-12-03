from DataBase_Project.SQLCreate import SQLCreate
from DataBase_Project.connect import connect

class CreateTableForUser:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def createHighSchoolTable(self, region):
        self.cursor.execute("DROP TABLE IF EXISTS HighSchoolScholarshipForUsers;")
        query = SQLCreate().createHighSchoolScholarshipForUser()
        self.cursor.execute(query, ('%' + region + '%',))
        self.con.commit()

    def createFacilityTable(self, region):
        self.cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        query = SQLCreate().createRegionToUsers()
        self.cursor.execute(query, ('%' + region + '%',))
        self.con.commit()
