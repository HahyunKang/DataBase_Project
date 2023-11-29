import psycopg2
import csv

from SQLCreate import SQLCreate
from connect import connect

def univMain():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS ScholarshipForUniv;")
        cursor.execute(
                 """CREATE TABLE ScholarshipForUniv (scholarshipId INT, cityName VARCHAR(128), univName VARCHAR(
                 128), scholarshipType VARCHAR(128), supportAmount FLOAT); """
             )
        with open('C:/Users/emma3/PycharmProjects/dbPorject/DataBase_Project/UnivScholarshipData.csv','r') as f:
             reader = csv.reader(f)
             next(reader)
             for row in reader:
                 cursor.execute(
                  "INSERT INTO ScholarshipForUniv (scholarshipId,cityName,univName,scholarshipType,supportAmount) VALUES (%s,%s,%s,%s,%s)",
                  row
                 )
        cursor.execute("SELECT * FROM ScholarshipForUniv")
        res = cursor.fetchall()
        for data in res:
            print(data)
        conn.commit()
        # cursor.close()
        # conn.close()
        cursor.execute("DROP TABLE IF EXISTS ScholarshipForUsers;")
        query = SQLCreate().createScholarShipForUser()
        cursor.execute(query)
        cursor.execute("SELECT * FROM ScholarshipForUsers;")
        res = cursor.fetchall()
        for data in res:
            print(data)
        conn.commit()
        # cursor.close()
        # conn.close()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e


if __name__ == "__main__":
    univMain()
