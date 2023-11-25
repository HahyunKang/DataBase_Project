import psycopg2
import csv

from connect import connect


def user():
    try:
        # # print("SQL Programming Test\n")
        # # port, user, password, database 는 각자의 환경에 맞게 입력
        # conn = psycopg2.connect(
        #     host="localhost",
        #     port="5432",
        #     user="postgres",
        #     password="4238",
        #     database="project"
        # )
        # print("Connecting PostgreSQL database\n")
        conn = connect()
        with conn:
            cur = conn.cursor()
            # cur.execute("""
            # CREATE TABLE Users(userId Int, name varchar, region varchar, schoolName varchar, age Int, password varchar, primary key(userId))
            # """)
            # cur.execute("INSERT INTO Users VALUES (1, '김지영', '서울', '서울고등학교', 18, 0000);")
            # cur.execute("INSERT INTO Users VALUES (2, '이승민', '부산', '부산대학교', 22, 0001);")
            # cur.execute("INSERT INTO Users VALUES (3, '박지수', '대구', '대구고등학교', 17, 0002);")
            # cur.execute("INSERT INTO Users VALUES (4, '최민호', '인천', '인하대학교', 21, 0003);")
            # cur.execute("INSERT INTO Users VALUES (5, '정지원', '광주', '광주고등학교', 19, 0004);")
            # cur.execute("INSERT INTO Users VALUES (6, '홍길동', '대전', '대전대학교', 20, 0005);")
            # cur.execute("INSERT INTO Users VALUES (7, '강나영', '화성', '능동고등학교', 18, 0006);")
            # cur.execute("INSERT INTO Users VALUES (8, '김철수', '강릉', '강릉대학교', 23, 0007);")
            # cur.execute("INSERT INTO Users VALUES (9, '박미정', '제주', '제주고등학교', 17, 0008);")
            # cur.execute("INSERT INTO Users VALUES (10, '최준호', '전주', '전북대학교', 24, 0009);")
            # cur.execute("INSERT INTO Users VALUES (11, '정은지', '울산', '울산고등학교', 19, 0010);")
            # cur.execute("INSERT INTO Users VALUES (12, '홍길동', '대전', '대전대학교', 20, 0011);")
            # cur.execute("INSERT INTO Users VALUES (13, '강승우', '안산', '안산고등학교', 18, 0012);")
            # cur.execute("INSERT INTO Users VALUES (14, '송지현', '수원', '수원대학교', 21, 0013);")
            # cur.execute("INSERT INTO Users VALUES (15, '임태영', '창원', '창원대학교', 24, 0014);")
            # cur.execute("INSERT INTO Users VALUES (16, '홍길동', '대전', '대전대학교', 20, 0015);")
            # cur.execute("INSERT INTO Users VALUES (17, '이나영', '세종', '세종고등학교', 18, 0016);")
            # cur.execute("INSERT INTO Users VALUES (18, '김철수', '강릉', '아주대학교', 23, 0017);")
            # cur.execute("INSERT INTO Users VALUES (19, '박미정', '제주', '제주고등학교', 17, 0018);")
            # cur.execute("INSERT INTO Users VALUES (20, '강민호', '전주', '전북대학교', 24, 0019);")
            # cur.execute("INSERT INTO Users VALUES (21, '이은지', '울산', '울산고등학교', 19, 0020);")
            # cur.execute("INSERT INTO Users VALUES (22, '김태민', '안산', '안산고등학교', 18, 0021);")
            # cur.execute("INSERT INTO Users VALUES (23, '송지원', '수원', '수원대학교', 21, 0022);")
            # cur.execute("INSERT INTO Users VALUES (24, '임경민', '창원', '창원대학교', 24, 0023);")
            # cur.execute("INSERT INTO Users VALUES (25, '오지훈', '김해', '부경대학교', 20, 0024);")
            # cur.execute("INSERT INTO Users VALUES (26, '윤가은', '안양', '안양대학교', 22, 0025);")
            # cur.execute("INSERT INTO Users VALUES (27, '나성민', '광주', '조선대학교', 23, 0026);")
            # cur.execute("INSERT INTO Users VALUES (28, '전주원', '포항', '포항공과대학교', 21, 0027);")
            # cur.execute("INSERT INTO Users VALUES (29, '김혜리', '대전', '충남대학교', 24, 0028);")
            # cur.execute("INSERT INTO Users VALUES (30, '이승우', '세종', '세종대학교', 22, 0029);")
            # cur.execute("INSERT INTO Users VALUES (31, '박은주', '강릉', '강릉대학교', 23, 0030);")
            # cur.execute("INSERT INTO Users VALUES (32, '최성민', '인천', '인하대학교', 21, 0031);")
            # cur.execute("INSERT INTO Users VALUES (33, '정유진', '광주', '전남대학교', 25, 0032);")
            # cur.execute("INSERT INTO Users VALUES (34, '강민정', '안산', '한국과학기술원', 22, 0033);")
            # cur.execute("INSERT INTO Users VALUES (35, '송상현', '수원', '성균관대학교', 23, 0034);")
            # cur.execute("INSERT INTO Users VALUES (36, '임재영', '창원', '경상대학교', 20, 0035);")
            # cur.execute("INSERT INTO Users VALUES (37, '오은지', '김해', '부경대학교', 22, 0036);")
            # cur.execute("INSERT INTO Users VALUES (38, '윤준호', '안양', '고려대학교', 23, 0037);")
            # cur.execute("INSERT INTO Users VALUES (39, '나다빈', '광주', '조선대학교', 21, 0038);")


    except psycopg2.Error as e:
        print("Connection failure.")
        raise e
    
if __name__ == "__main__":
    user()