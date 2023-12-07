import select

from prettytable import PrettyTable

from SQLInsert import SQLInsert
from SQLSelect import SQLSelect
from connect import connect


class ScholarshipController:
    def __init__(self):
        self.select = SQLSelect()
        self.insert = SQLInsert()
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def getUnivScholarship(self, userId):
        query = self.select.selectUnivScholashipInfo(userId)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def apply(self, userId, scholarshipId):
        query = self.insert.insertApplication()
        self.cursor.execute(query, (userId, scholarshipId,))
        self.con.commit()

    def getUnivApplication(self, userId):
        query = self.select.selectApplicationForUniv(userId)
        self.cursor.execute(query)
        self.con.commit()
        data = self.cursor.fetchall()
        return data

    def getHighSchoolScholarship(self, userId):
        query = self.select.selectHighSchoolScholashipInfo(userId)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def getHighSchoolApplication(self, userId):
        query = self.select.selectApplicationForHighSchool(userId)
        self.cursor.execute(query)
        self.con.commit()
        data = self.cursor.fetchall()
        return data

