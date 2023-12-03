import psycopg2
import csv

from DataBase_Project.connect import connect


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

        with open("C:/Users/emma3/OneDrive - Ajou University/바탕 화면/c언어/2023.2/ScholarshipForHighSchool.csv", 'r') as f:
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

            cur.execute("SELECT * FROM ScholarshipForHighSchool;")
            res = cur.fetchall()
            for data in res:
                print(data)
            conn.commit()

    except psycopg2.Error as e:
        print("Connection failure.")
        raise e
    
if __name__ == "__main__":
    main()