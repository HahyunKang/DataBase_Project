import psycopg2
import csv

from connect import connect
from connect import connect


def facility():
    try:
        conn = connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS WellfareFacility;")
            cursor.execute(
                """CREATE TABLE WellfareFacility (facilityId INT, facilityName VARCHAR(128), zipCode INT, address VARCHAR(
                256), phoneNum VARCHAR(256), homepageUrl VARCHAR(256)); """
            )
        with open('C:/WellfareFacility.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor.execute(
                "INSERT INTO WellfareFacility (facilityId,facilityName,zipCode,address,phoneNum,homepageUrl) VALUES (%s,%s,%s,%s,%s,%s)",
                row
            )
            conn.commit()


            #---------- 실행 잘 되는 코드-------------------------------------
            # cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
            # query = SQLCreate().createRegionToUsers()
            # cursor.execute(query, ('%' + region + '%',))
            # cursor.execute("SELECT * FROM FacilityForUsers;")
            # res = cursor.fetchall()
            # for data in res:
            #     print(data)
            # conn.commit()

            # query = "SELECT * FROM WellfareFacility WHERE address LIKE %s;"
            # cursor.execute(query, ('%' + region + '%',))
            # query = cursor.fetchall()
            # return query
            #----------------------------------------------------------------
            # cursor.execute("SELECT * FROM WellfareFacility")
            # cursor.execute("DROP TABLE IF EXISTS FacilityForUsers;")
            # query = SQLCreate().createRegionToUsers()
            # cursor.execute(query, ('%' + region + '%',))
            # cursor.execute("SELECT * FROM FacilityForUsers;")
            # conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e
#
if __name__ == "__main__":
    facility()