from SQL.SQLSelect import SQLSelect
from common.connect import connect


class SchoolInfoController:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def getSchoolName(self, userId):
        sqlSelect = SQLSelect()
        schoolName = sqlSelect.selectSchool(userId)
        self.cursor.execute(schoolName)
        data = self.cursor.fetchall()
        extracted_data = data[0][0]
        return extracted_data




