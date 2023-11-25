import csv
import psycopg2

def facilityMain():
 try:
   conn = psycopg2.connect(
   host="localhost",
   port="5432",
   user="postgres",
   password="0442",
   database="postgres"
  )
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
   cursor.execute("SELECT * FROM WellfareFacility")
   res = cursor.fetchall()
   for data in res:
       print(data)


 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

if __name__ == "__main__":
 facilityMain()