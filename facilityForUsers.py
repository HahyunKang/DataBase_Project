import psycopg2
from SQLSelect import SQLSelect
import Login

from connect import connect


def facilityMain():
 try:
   conn = connect()
   with conn:
        # 테이블 생성
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        cursor.execute("CREATE TABLE FacilityForUsers (userId int, facilityId int);")
        print(Login.userName, Login.userRegion)
        selectFacility = SQLSelect().insertRegionToUsers(Login.userName, Login.userRegion)
        cursor.execute(selectFacility)

        cursor.execute("SELECT * FROM FacilityForUsers;")
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