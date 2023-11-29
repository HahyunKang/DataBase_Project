from SQLSelect import SQLSelect
from connect import connect


class CommunityController:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()

    def getCommunityName(self, userId):
        sqlSelect = SQLSelect()
        communityName = sqlSelect.selectCommunity(userId)
        self.cursor.execute(communityName)
        data = self.cursor.fetchall()
        extracted_data = data[0][0]
        return extracted_data

    def posting(self,userId):
        print()

