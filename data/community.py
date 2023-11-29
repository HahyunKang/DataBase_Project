import psycopg2
import csv

from DataBase_Project.connect import connect


def community():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Community;")
        cursor.execute(
            """CREATE TABLE Community (communityID Int, userId Int, communityName VARCHAR ); """
        )

        cursor.execute("""
            INSERT INTO Community (communityId, userId, communityName)
            SELECT r.regionId, u.userId, r.regionName || '게시판'
            FROM Users u
            JOIN region r ON u.region = r.regionName;
        """)
        cursor.execute("select * from Community;")
        res = cursor.fetchall()
        for data in res:
            print(data)
        conn.commit()



    except psycopg2.Error as e:
        print("Connection failure.")
        raise e







if __name__ == "__main__":
    community()