import psycopg2

from connect import connect


def community():
    try:
        conn = connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS Community;")
            cursor.execute(
                """CREATE TABLE Community (regionId INT, userId INT, communityName VARCHAR(256), primary key (regionId); """
            )
            conn.commit()

            cursor.execute("INSERT INTO Community VALUES (1, '김지영', '서울', '서울고등학교', 18, 0000);")

            #---------- 실행 잘 되는 코드-------------------------------------

            # cursor.execute("SELECT * FROM Community")
            # res = cursor.fetchall()
            # for data in res:
            #     print(data)


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

# if __name__ == "__main__":
#     facility(region)