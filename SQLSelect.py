class SQLSelect:
    def __init__(self):
        self.res = None

    def selectUser(self, username, password):
        query = f"SELECT * FROM Users WHERE name = '{username}' AND password = '{password}'"
        return query



