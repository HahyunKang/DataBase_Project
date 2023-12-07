import psycopg2
import csv

from connect import connect
from prettytable import PrettyTable


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
        columns = [desc[0] for desc in cursor.description]
        table = PrettyTable(columns)
        for data in res:
            table.add_row(data)
        print(table)


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
    region()