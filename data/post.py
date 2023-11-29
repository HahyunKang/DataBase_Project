import psycopg2
import csv

from DataBase_Project.connect import connect


def post():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Post;")
        cursor.execute(
              """CREATE TABLE Post (postId SERIAL, writerId INT, title VARCHAR, content VARCHAR, regionId INT, hits INT, primary key(postId)); """
        )
        conn.commit()
        cursor.execute("INSERT INTO Post(writerId, title, content, regionId, hits) VALUES (3, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 3 = Community.userId), 7);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (1, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 9);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (4, '행복하고 싶다', (SELECT Community.communityId FROM Community where 4 = Community.userId),'우울해', 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (100, '데베 재밌다', (SELECT Community.communityId FROM Community where 100 = Community.userId),'개꿀잼', 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (50, '나같은 사람 또 있나',(SELECT Community.communityId FROM Community where 50 = Community.userId), '사는 게 힘들어', 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (4, '행복하고 싶다', (SELECT Community.communityId FROM Community where 4 = Community.userId),'어떡하죠ㅠ', 6);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (3, '장학금 받았어요',(SELECT Community.communityId FROM Community where 1 = Community.userId), '댓글 달면 공유해드림ㅇㅇ', 8);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (3, '사회복지시설 후기', (SELECT Community.communityId FROM Community where 1 = Community.userId),'심심해요ㅠㅠ', 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (20, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (14, '헉', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (18, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (23, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (40, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (31, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (13, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (33, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (12, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (15, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (1, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (12, '받았어요ㅎㅎ', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (19, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (99, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (96, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (48, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (81, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (39, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (40, '받았어요ㅎ', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (56, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (96, '헉', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (79, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (78, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (45, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 15, 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (34, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (29, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (14, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (45, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (11, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (14, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (16, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (30, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (15, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (38, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (18, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (15, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (49, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (13, '헉', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (19, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (23, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (56, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (79, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (34, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 20);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (69, '사회복지시설 후기', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (34, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (60, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (55, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (49, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (68, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (34, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (20, 'help', '댓글 달면 공유해드림ㅇㅇㅋ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (54, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (69, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (28, '받았어요ㅋ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (44, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (44, 'help', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (13, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (89, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (68, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (67, '심심해요ㅠㅠ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (69, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (12, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (33, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (11, '받았어요ㅋ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (12, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (15, '사회복지시설 후기', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (16, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (99, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (100, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (33, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (14, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (25, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (78, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (35, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (47, '심심해요ㅠㅠ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (36, '무제', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (32, '심심해요ㅠㅠ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (45, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (59, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (78, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (43, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content, hits) VALUES (22, '사회복지시설 후기', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 2);")


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