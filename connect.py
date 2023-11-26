import psycopg2

def connect():
 try:
   conn = psycopg2.connect(
   host="localhost",
   port="5432",
   user="postgres",
   password="4238",
   database="project"
   )
   return conn

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

