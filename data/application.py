import psycopg2

from connect import connect


def application():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Application;")
        cursor.execute(
            """CREATE TABLE Application (userId INT, scholarshipId INT); """
        )
        conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e


if __name__ == "__main__":
    application()
