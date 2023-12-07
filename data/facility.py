import psycopg2
import csv

from prettytable import PrettyTable

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

            cursor.execute("SELECT * FROM WellfareFacility")
            res = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            table = PrettyTable(columns)
            for data in res:
                table.add_row(data)
            print(table)

    except psycopg2.Error as e:
        print("Connection failure.")
        raise e
#
if __name__ == "__main__":
    facility()