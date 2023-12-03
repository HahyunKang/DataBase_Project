class SQLInsert:
    def __init__(self):
        self.res = None

    def insertPostView(self,postId):
        query = "INSERT INTO PostView (postId) VALUES (%s)"
        return query

    def insertPost(self):
        query = "INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (%s,%s,%s, (SELECT Community.communityId FROM Community where %s = Community.userId), 0);"
        return query
