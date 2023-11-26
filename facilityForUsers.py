import psycopg2
from SQLSelect import SQLSelect

from connect import connect


def facilityMain(userName, userRegion, userId):
 try:
   conn = connect()
   with conn:
        # 테이블 생성
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        cursor.execute("CREATE TABLE FacilityForUsers (userId int, facilityId int);")

        # n = userName
        # r = userRegion

        # print("TEST"+n, r)

        #
        insertFacility = SQLSelect().insertRegionToUsers(userRegion, userName)
        cursor.execute(insertFacility)
        query = cursor.fetchall()
        for i in query:
            print(i)
        
        selectFacility = SQLSelect().selectRegionToUsers(userId)
        query = cursor.fetchall()
        for i in query:
          print(i)
        # query = cursor.fetchall()
        # for data in query:
        #     print(data)

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 facilityMain()