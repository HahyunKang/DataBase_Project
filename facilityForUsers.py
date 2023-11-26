import psycopg2
from SQLSelect import SQLSelect
from Login import login

from connect import connect


def facilityMain():
 try:
   conn = connect()
   with conn:
        # 테이블 생성
        cursor = conn.cursor()
        # cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        # cursor.execute("CREATE TABLE FacilityForUsers (userId int, facilityId int);")

        #
        userName, userRegion = login()
        SQLSelect().selectUserRegion(userName)
        SQLSelect().selectFacilityForUsers(userRegion)
        res = cursor.fetchall()
        for data in res:
            print(data)

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 facilityMain()