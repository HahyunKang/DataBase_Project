class SQLInsert:
    def __init__(self):
        self.res = None

    def insertPostView(self,postId):
        query = "INSERT INTO PostView (postId) VALUES (%s)"
        return query