from DataBase_Project.connect import connect


class View:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def printUnivScholarInfo(self, query):
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        for data in query:
            print(data)

    def printFacilityInfo(self, query):
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        for data in query:
            print(data)