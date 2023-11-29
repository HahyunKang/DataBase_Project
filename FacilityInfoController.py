from SQLSelect import SQLSelect
from connect import connect


class FacilityInfoController:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def getFacilityName(self, userId):
        sqlSelect = SQLSelect()
        facilityName = sqlSelect.selectFacility(userId)
        self.cursor.execute(facilityName)
        data = self.cursor.fetchall()
        extracted_data = data[0][0]
        return extracted_data




