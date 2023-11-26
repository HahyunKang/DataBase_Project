class SQLSelect:
    def __init__(self):
        self.res = None

    # 로그인을 위한 함수 ------------------------------------------------------------------------
    def selectUser(self, username, password):
        query = f"SELECT * FROM Users WHERE name = '{username}' AND password = '{password}'" 
        return query 

    def selectUserName(self, username): 
        query = f"SELECT name FROM Users WHERE name = '{username}'" 
        return query 

    def selectUserRegion(self, username):
        query = f"SELECT region FROM Users WHERE name = '{username}'"
        return query
    #------------------------------------------------------------------------------------------------
    
    # 사회 복지 시설을 위한 함수 ----------------------------------------------------------------------
    # def insertRegionToUsers(self, userName, region):
    #     query = f"""INSERT INTO FacilityForUsers
    #                 SELECT facilityId, userId
    #                 FROM WellfareFacility, Users
    #                 WHERE address like '%{region}%' AND name = '{userName}';
    #             """
    #     return query

    def insertRegionToUsers(self, name, region):
        query = f"""INSERT INTO FacilityForUsers
                    SELECT facilityId, userId
                    FROM WellfareFacility, Users
                    WHERE address like '%{region}%' AND name = '{name}';
                    """
        
        return query
    
    # def selectRegionToUsers(self, id):
    #     query = f"""SELECT *
    #                 FROM  WellfareFacility
    #                 WHERE facilityId IN (
    #                     SELECT facilityId
    #                     FROM FacilityForUsers
    #                     WHERE userId = '{id}'
    #                 )
    #                 """
    #     return query
    
    #-------------------------------------------------------------------------------------------------
