import psycopg2
import csv

from connect import connect


def post():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Post;")
        cursor.execute(
              """CREATE TABLE Post (postId SERIAL, writerId INT, title VARCHAR, content VARCHAR, regionId INT, hits INT, primary key(postId)); """
        )
        conn.commit()
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (3, '무제', '심심해요ㅠㅠ', 29, 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (1, 'help', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (4, '행복하고 싶다', '우울해', 3, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (100, '데베 재밌다', '개꿀잼', 1, 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (50, '나같은 사람 또 있나', '사는 게 힘들어', 3, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (4, '행복하고 싶다', '어떡하죠ㅠ', 6, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (3, '장학금 받았어요', '댓글 달면 공유해드림ㅇㅇ', 8, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (3, '사회복지시설 후기', '심심해요ㅠㅠ', 29, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (20, '헉', '어떡하죠ㅠ', 2, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (14, '헉', 'ㅈㄱㄴ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (18, 'help', '댓글 달면 공유해드림ㅇㅇ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (23, 'help', 'ㅈㄱㄴ', 13, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (40, '헉', '어떡하죠ㅠ', 23, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (31, '무제', '심심해요ㅠㅠ', 6, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (13, 'help', '어떡하죠ㅠ', 8, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (33, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (12, 'help', 'ㅈㄱㄴ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (15, 'help', '어떡하죠ㅠ', 20, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (1, '사회복지시설 후기', '어떡하죠ㅠ', 4, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (12, '받았어요ㅎㅎ', '댓글 달면 공유해드림ㅇㅇ', 6, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (35, '무제', '심심해요ㅠㅠ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (19, '헉', '어떡하죠ㅠ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (99, 'help', 'ㅈㄱㄴ', 7, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (96, '헉', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (48, 'help', 'ㅈㄱㄴ', 24, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (81, '헉', '어떡하죠ㅠ', 6, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (39, '사회복지시설 후기', '어떡하죠ㅠ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (40, '받았어요ㅎ', '댓글 달면 공유해드림ㅇㅇ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (56, 'help', '어떡하죠ㅠ', 3, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (96, '헉', 'ㅈㄱㄴ', 5, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (79, 'help', 'ㅈㄱㄴ', 24, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (78, '행복하고 싶다', '어떡하죠ㅠ', 6, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (45, 'help', 'ㅈㄱㄴ', 15, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, '헉', '어떡하죠ㅠ', 4, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (34, '무제', '심심해요ㅠㅠ', 25, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (29, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (14, 'help', 'ㅈㄱㄴ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (45, 'help', '어떡하죠ㅠ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (11, 'help', 'ㅈㄱㄴ', 24, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (14, '사회복지시설 후기', '어떡하죠ㅠ', 5, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (16, 'help', '어떡하죠ㅠ', 13, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (30, '무제', '심심해요ㅠㅠ', 6, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (15, 'help', 'ㅈㄱㄴ', 10, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (38, '행복하고 싶다', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (18, 'help', 'ㅈㄱㄴ', 4, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (15, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ', 18, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (49, 'help', 'ㅈㄱㄴ', 21, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (13, '헉', 'ㅈㄱㄴ', 26, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (35, '무제', '심심해요ㅠㅠ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (19, 'help', '어떡하죠ㅠ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (23, '사회복지시설 후기', '어떡하죠ㅠ', 2, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (56, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', 23, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, 'help', 'ㅈㄱㄴ', 16, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (79, '행복하고 싶다', '어떡하죠ㅠ', 3, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (34, 'help', 'ㅈㄱㄴ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, '무제', '심심해요ㅠㅠ', 21, 20);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (69, '사회복지시설 후기', 'ㅈㄱㄴ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (34, 'help', '어떡하죠ㅠ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (60, '헉', '어떡하죠ㅠ', 2, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (55, 'help', 'ㅈㄱㄴ', 30, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (49, '사회복지시설 후기', '어떡하죠ㅠ', 24, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (68, 'help', '어떡하죠ㅠ', 21, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (34, '무제', '심심해요ㅠㅠ', 5, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (20, 'help', '댓글 달면 공유해드림ㅇㅇㅋ', 13, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (54, '받았어요ㅋ', '어떡하죠ㅠ', 2, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (69, 'help', 'ㅈㄱㄴ', 4, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (28, '받았어요ㅋ', '어떡하죠ㅠ', 1, 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (44, '사회복지시설 후기', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (44, 'help', '댓글 달면 공유해드림ㅇㅇ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (35, '무제', '심심해요ㅠㅠ', 29, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (13, 'help', '어떡하죠ㅠ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (89, '받았어요ㅋ', 'ㅈㄱㄴ', 26, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (68, 'help', '어떡하죠ㅠ', 15, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (67, '심심해요ㅠㅠ', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (69, '사회복지시설 후기', '어떡하죠ㅠ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (12, 'help', '어떡하죠ㅠ', 12, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (33, '무제', '심심해요ㅠㅠ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (11, '받았어요ㅋ', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (12, 'help', '댓글 달면 공유해드림ㅇㅇ', 10, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (15, '사회복지시설 후기', 'ㅈㄱㄴ', 25, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (16, 'help', '어떡하죠ㅠ', 7, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (99, '받았어요ㅋ', 'ㅈㄱㄴ', 16, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (100, 'help', '어떡하죠ㅠ', 9, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (33, '무제', '심심해요ㅠㅠ', 29, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (14, 'help', 'ㅈㄱㄴ', 4, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (25, '사회복지시설 후기', '어떡하죠ㅠ', 14, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (78, '받았어요ㅋ', '어떡하죠ㅠ', 20, 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, 'help', 'ㅈㄱㄴ', 29, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (35, '받았어요ㅋ', '어떡하죠ㅠ', 30, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (47, '심심해요ㅠㅠ', 'ㅈㄱㄴ', 1, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (36, '무제', '댓글 달면 공유해드림ㅇㅇ', 29, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, '사회복지시설 후기', '어떡하죠ㅠ', 2, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (32, '심심해요ㅠㅠ', '어떡하죠ㅠ', 4, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (45, '받았어요ㅋ', 'ㅈㄱㄴ', 15, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', 10, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (59, 'help', '댓글 달면 공유해드림ㅇㅇ', 26, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (78, '사회복지시설 후기', '어떡하죠ㅠ', 13, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (43, 'help', '어떡하죠ㅠ', 10, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (22, '사회복지시설 후기', '댓글 달면 공유해드림ㅇㅇ', 12, 2);")



        cursor.execute("SELECT * FROM Post")
        conn.commit()
        res = cursor.fetchall()
        for data in res:
            print(data)
        conn.commit()


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
    post()