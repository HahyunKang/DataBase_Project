import psycopg2
import csv

from connect import connect
from prettytable import PrettyTable


def univMain():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS ScholarshipForUniv;")
        cursor.execute(
                 """CREATE TABLE ScholarshipForUniv (scholarshipId INT, cityName VARCHAR(128), univName VARCHAR(
                 128), scholarshipType VARCHAR(128), supportAmount FLOAT); """
             )
        with open('C:/UnivScholarshipData.csv','r') as f:
             reader = csv.reader(f)
             next(reader)
             for row in reader:
                 cursor.execute(
                  "INSERT INTO ScholarshipForUniv (scholarshipId,cityName,univName,scholarshipType,supportAmount) VALUES (%s,%s,%s,%s,%s)",
                  row
                 )

        cursor.execute("SELECT * FROM ScholarshipForUniv")
        res = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        table = PrettyTable(columns)
        for data in res:
            table.add_row(data)
        print(table)
        cursor.close()
        conn.close()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e


if __name__ == "__main__":
    univMain()
