import csv
import psycopg2

from connect import connect


def facilityMain():
 try:
   conn = connect()
   with conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
        cursor.execute("CREATE TABLE FacilityForUsers (userId int, facilityId int);")
        cursor.execute("SELECT * FROM WellfareFacility")
        res = cursor.fetchall()
        for data in res:
            print(data)

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 facilityMain()