import csv
import psycopg2

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
        with open('C:/Users/emma3/OneDrive - Ajou University/바탕 화면/c언어/2023.2/WellfareFacility.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cursor.execute(
                "INSERT INTO WellfareFacility (facilityId,facilityName,zipCode,address,phoneNum,homepageUrl) VALUES (%s,%s,%s,%s,%s,%s)",
                row
            )
            cursor.execute("SELECT * FROM WellfareFacility")
            res = cursor.fetchall()
            for data in res:
                print(data)

            # search_term = '화성'

            # query = "SELECT facilityName FROM WellfareFacility WHERE address LIKE %s;"
            # cursor.execute(query, ('%' + search_term + '%',))
            # query = cursor.fetchall()
            # for i in query:
            #     print(i)


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
 facility()