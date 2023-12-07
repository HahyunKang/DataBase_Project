import psycopg2
import csv

from prettytable import PrettyTable

from connect import connect


def post():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS Post;")
        cursor.execute(
              """CREATE TABLE Post (postId SERIAL, writerId INT, title VARCHAR, content VARCHAR, regionId INT, hits INT, primary key(postId)); """
        )
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (3, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 3 = Community.userId), 7);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (1, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 9);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (4, '행복하고 싶다', '우울해', (SELECT Community.communityId FROM Community where 4 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (100, '데베 재밌다', '개꿀잼',(SELECT Community.communityId FROM Community where 100 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (50, '나같은 사람 또 있나', '사는 게 힘들어',(SELECT Community.communityId FROM Community where 50 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (4, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 4 = Community.userId), 6);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (3, '장학금 받았어요','댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 3 = Community.userId), 8);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (3, '사회복지시설 후기', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 3 = Community.userId),1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (20, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 20 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (14, '헉', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 14 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (18, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 18 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 19 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (23, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 23 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (40, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 40 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (31, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 31 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (13, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 13 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (33, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 33 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (12, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 12 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (15, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 15 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (1, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 1 = Community.userId), 5);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (12, '받았어요ㅎㅎ', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 12 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 35 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (19, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 19 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (99, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 99 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (96, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 96 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (48, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 48 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (81, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 81 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (39, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 39 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (40, '받았어요ㅎ', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 40 = Community.userId), 5);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (56, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 56 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (96, '헉', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 96 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (79, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 79 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (78, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 78 = Community.userId),4);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (45, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 45 = Community.userId), 15);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, '헉', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 59 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (34, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 34 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (29, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 29 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (14, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 14 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (45, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 45 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (11, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 11 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (14, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 14 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (16, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 16 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (30, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 30 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (15, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 15 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (38, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 38 = Community.userId), 9);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (18, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 18 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (15, '받았어요ㅋ', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 15 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (49, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 49 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (13, '헉', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 13 = Community.userId), 4);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 35 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (19, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 19 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (23, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 23 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (56, '행복하고 싶다', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 56 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 59 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (79, '행복하고 싶다', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 79 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (34, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 34 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 59= Community.userId), 20);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (69, '사회복지시설 후기', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 69 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (34, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 34 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (60, '헉', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 60 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (55, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 55 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (49, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 49 = Community.userId),1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (68, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 68 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (34, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 34 = Community.userId),4);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (20, 'help', '댓글 달면 공유해드림ㅇㅇㅋ', (SELECT Community.communityId FROM Community where 20 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (54, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 54 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (69, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 69 = Community.userId),1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (28, '받았어요ㅋ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 28 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (44, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 44 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (44, 'help', '댓글 달면 공유해드림ㅇㅇ',(SELECT Community.communityId FROM Community where 44 = Community.userId), 6);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (35, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 35 = Community.userId), 7);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (13, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 13 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (89, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 89 = Community.userId),8);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (68, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 68 = Community.userId),1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (67, '심심해요ㅠㅠ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 67 = Community.userId), 9);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (69, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 69 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (12, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 12 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (33, '무제', '심심해요ㅠㅠ',(SELECT Community.communityId FROM Community where 33 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (11, '받았어요ㅋ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 11 = Community.userId),5);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (12, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 12 = Community.userId),6);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (15, '사회복지시설 후기', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 15 = Community.userId), 2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (16, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 16 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (99, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 99 = Community.userId), 6);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (100, 'help', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 100 = Community.userId),7);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (33, '무제', '심심해요ㅠㅠ', (SELECT Community.communityId FROM Community where 33 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (14, 'help', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 14 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (25, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 25 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (78, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 78 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, 'help', 'ㅈㄱㄴ',(SELECT Community.communityId FROM Community where 59 = Community.userId), 0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (35, '받았어요ㅋ', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 35 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (47, '심심해요ㅠㅠ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 47 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (36, '무제', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 36 = Community.userId),0);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, '사회복지시설 후기', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 59 = Community.userId),2);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (32, '심심해요ㅠㅠ', '어떡하죠ㅠ',(SELECT Community.communityId FROM Community where 32 = Community.userId), 4);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (45, '받았어요ㅋ', 'ㅈㄱㄴ', (SELECT Community.communityId FROM Community where 45 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (19, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 19 = Community.userId), 3);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (59, 'help', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 59 = Community.userId), 1);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (78, '사회복지시설 후기', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 78 = Community.userId), 6);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (43, 'help', '어떡하죠ㅠ', (SELECT Community.communityId FROM Community where 43 = Community.userId), 7);")
        cursor.execute("INSERT INTO Post(writerId, title, content,  regionId, hits ) VALUES (22, '사회복지시설 후기', '댓글 달면 공유해드림ㅇㅇ', (SELECT Community.communityId FROM Community where 22 = Community.userId), 0);")
        conn.commit()


        cursor.execute("SELECT * FROM Post")
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
    post()