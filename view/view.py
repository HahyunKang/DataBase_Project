from common.connect import connect


class view:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def printUnivScholarInfo(self, query):
        self.cursor.execute(query)
        query = self.cursor.fetchall()
        for data in query:
            print(data)

