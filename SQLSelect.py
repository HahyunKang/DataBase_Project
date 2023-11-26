class SQLSelect:
    def __init__(self):
        self.res = None

    def selectUser(self, username, password):
        query = f"SELECT * FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query

    def selectUniv(self, univName):
        query = f"SELECT * FROM Users WHERE univName = '{univName}'"
        return query

    def selectUserRegion(self, username, password):
        query = f"SELECT region FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query

    def selectFacilityForUsers(self, region):
        query = f"SELECT * FROM WellfareFacility WHERE address like '%{region}%'"
        return query


