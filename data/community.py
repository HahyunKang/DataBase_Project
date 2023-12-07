import psycopg2
import csv

from prettytable import PrettyTable

from connect import connect


def community():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Community;")
        cursor.execute(
            """CREATE TABLE Community (communityId Int, userId Int, communityName VARCHAR ); """
        )

        cursor.execute("""
            INSERT INTO Community (communityId, userId, communityName)
            SELECT r.regionId, u.userId, r.regionName || '게시판'
            FROM Users u
            JOIN region r ON u.region = r.regionName;
        """)
        cursor.execute("select * from Community;")
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
    community()