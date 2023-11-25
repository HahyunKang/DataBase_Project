import csv
import psycopg2
from main import main


def univMain():
 try:
  conn = main()
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
  for data in res:
      print(data)


 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 univMain()