import psycopg2
import csv

from DataBase_Project.connect import connect


def region():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Region;")
        cursor.execute(
                 """CREATE TABLE Region (regionId SERIAL PRIMARY KEY,regionName VARCHAR(128)); """
             )
        cursor.execute(
              "INSERT INTO Region (regionName) SELECT DISTINCT Region FROM users ORDER BY REGION "
        )
        cursor.execute("SELECT * FROM Region")
        conn.commit()
        res = cursor.fetchall()
        for data in res:
            print(data)
        conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
    region()