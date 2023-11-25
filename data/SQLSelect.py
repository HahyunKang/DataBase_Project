class SQLSelect:
    def __init__(self):
        self.res = 0
    def selectUser(name,password):
        query = f"SELECT * FROM User WHERE userName = '{name}'"
        return query