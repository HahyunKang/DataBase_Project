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
        # i = userId

        # print("TEST"+n, r, i)

        # facilityForUsers 테이블에 정보 넣기
        insertFacility = SQLSelect().insertRegionToUsers(userName, userRegion)
        cursor.execute(insertFacility, ('%' + userRegion + '%',))
        query = cursor.fetchall()
        for i in query:
            print(i)
        
        # # facilityForUser 테이블의 정보를 바탕으로 facility 정보들 모두 출력
        # selectFacility = SQLSelect().selectRegionToUsers(userId)
        # query = cursor.fetchall(selectFacility)
        # for i in query:
        #   print(i)
        # query = cursor.fetchall()
        # for data in query:
        #     print(data)

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 facilityMain()