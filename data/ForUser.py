from SQLCreate import SQLCreate
from connect import connect


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
