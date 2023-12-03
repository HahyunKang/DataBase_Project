import psycopg2

from DataBase_Project.connect import connect


def postView():
    try:
        conn = connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS PostView;")
            cursor.execute(
                """CREATE TABLE PostView (viewId SERIAL PRIMARY KEY,postId Int);"""
            )
            cursor.execute("""CREATE OR REPLACE FUNCTION updateViewCount() RETURNS TRIGGER AS $$ BEGIN UPDATE post set hits = 
            hits+1 where postId= New.postId; Return New; End; $$ LANGUAGE plpgsql""")
            cursor.execute("""CREATE TRIGGER increment_view_count after insert on postView for each row execute 
            function updateViewCount()""")
            conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e


if __name__ == "__main__":
    postView()
