import psycopg2

def main():
 try:
   conn = psycopg2.connect(
   host="localhost",
   port="5432",
   user="postgres",
   password="0442",
   database="postgres"
   )
   return conn

 except psycopg2.Error as e:
  print("Connection failure.")
  raise e

