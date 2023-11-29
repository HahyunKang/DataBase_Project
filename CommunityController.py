from SQLInsert import SQLInsert
from SQLSelect import SQLSelect
from connect import connect


class CommunityController:
    def __init__(self):
        self.res = None
        self.con = connect()
        self.cursor = self.con.cursor()
        self.select = SQLSelect()
        self.insert = SQLInsert()

    def getCommunityName(self, userId):
        sqlSelect = SQLSelect()
        communityName = sqlSelect.selectCommunity(userId)
        self.cursor.execute(communityName)
        data = self.cursor.fetchall()
        extracted_data = data[0][0]
        return extracted_data

    def getPostings(self,userId):
        self.cursor.execute(self.select.selectCommunityId(userId))
        communityId = self.cursor.fetchall()[0][0]
        self.cursor.execute(self.select.selectPostings(communityId))
        postings = self.cursor.fetchall()
        return postings

    def viewPost(self,postId):
        self.cursor.execute(self.insert.insertPostView(postId), (postId,))
        self.con.commit()

