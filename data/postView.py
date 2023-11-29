import psycopg2

from connect import connect


def postView():
    try:
        conn = connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS PostView;")
            cursor.execute(
                """CREATE TABLE PostView (viewId SERIAL PRIMARY KEY,postId Int);"""
            )
            conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
    postView()