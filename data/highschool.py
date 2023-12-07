import psycopg2
import csv

from prettytable import PrettyTable

from connect import connect
from data.ForUser import CreateTableForUser


def main():
    try:
        # print("SQL Programming Test\n")
        # port, user, password, database 는 각자의 환경에 맞게 입력
        conn = connect()
        # print("Connecting PostgreSQL database\n")
        with conn:
            cur = conn.cursor()

            cur.execute("DROP TABLE IF EXISTS ScholarshipForHighSchool;") # 만약 이미 table이 있다면 삭제
            cur.execute("""
            CREATE TABLE ScholarshipForHighSchool(scholarshipId Int, institutionName varchar, productName varchar,
            institutionType varchar, productType varchar, scholarType varchar, grade varchar, supportAmount varchar, primary key(scholarshipId))
            """)

        with open("C:/ScholarshipForHighSchool.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row.
            for row in reader:
                cur.execute(
                """
                INSERT INTO ScholarshipForHighSchool(scholarshipId, institutionName, productName, institutionType,
                productType, scholarType, grade, supportAmount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                row
                )
            conn.commit()

        cur.execute("SELECT * FROM ScholarshipForHighSchool")
        conn.commit()
        res = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        table = PrettyTable(columns)
        for data in res:
            table.add_row(data)
        print(table)





    except psycopg2.Error as e:
        print("Connection failure.")
        raise e
    
if __name__ == "__main__":
    main()