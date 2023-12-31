import psycopg2

from DataBase_Project.connect import connect


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
                #     CREATE TABLE Users(userId Int, name varchar, region varchar, schoolName varchar, age Int, password Int, primary key(userId))
                #     """)
                cur.execute("""SELECT * FROM Users""")
                res = cur.fetchall()
                for data in res:
                    print(data)
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
                # cur.execute("INSERT INTO Users VALUES (40, '강하현', '성남', '아주대학교', 22, 0039);")
                # cur.execute("INSERT INTO Users VALUES (41, '조은채', '화성', '아주대학교', 20, 0040);")
                # cur.execute("INSERT INTO Users VALUES (42, '이유정', '성남', '아주대학교', 21, 0041);")
                # cur.execute("INSERT INTO Users VALUES (43, '이해주', '논산', '아주대학교', 23, 0042);")
                # cur.execute("INSERT INTO Users VALUES (44, '옥채윤', '목포', '아주대학교', 20, 0043);")
                # cur.execute("INSERT INTO Users VALUES (45, '이태걸', '포항', '아주대학교', 23, 0044);")
                # cur.execute("INSERT INTO Users VALUES (46, '최주석', '대구', '아주대학교', 24, 0045);")
                # cur.execute("INSERT INTO Users VALUES (47, '윤정인', '수원', '아주대학교', 21, 0046);")
                # cur.execute("INSERT INTO Users VALUES (48, '손채린', '의왕', '아주대학교', 22, 0047);")
                # cur.execute("INSERT INTO Users VALUES (49, '고유진', '수원', '아주대학교', 22, 0048);")
                # cur.execute("INSERT INTO Users VALUES (50, '한동엽', '인천', '아주대학교', 22, 0049);")
                # cur.execute("INSERT INTO Users VALUES (51, '전형은', '안양', '아주대학교', 21, 0050);")
                # cur.execute("INSERT INTO Users VALUES (52, '김태규', '서울', '아주대학교', 25, 0051);")
                # cur.execute("INSERT INTO Users VALUES (53, '성민제', '고양', '아주대학교', 22, 0052);")
                # cur.execute("INSERT INTO Users VALUES (54, '김지현', '용인', '아주대학교', 21, 0053);")
                # cur.execute("INSERT INTO Users VALUES (55, '신세희', '수원', '아주대학교', 23, 0054);")
                # cur.execute("INSERT INTO Users VALUES (56, '이원행', '용인', '아주대학교', 23, 0055);")
                # cur.execute("INSERT INTO Users VALUES (57, '최예솔', '제주', '아주대학교', 22, 0056);")
                # cur.execute("INSERT INTO Users VALUES (58, '하효령', '수원', '아주대학교', 24, 0057);")
                # cur.execute("INSERT INTO Users VALUES (59, '김다정', '대전', '아주대학교', 21, 0058);")
                # cur.execute("INSERT INTO Users VALUES (60, '김종환', '천안', '아주대학교', 23, 0059);")
                # cur.execute("INSERT INTO Users VALUES (61, '이솔', '수원', '아주대학교', 20, 0060);")
                # cur.execute("INSERT INTO Users VALUES (62, '박솔', '성남', '아주대학교', 23, 0061);")
                # cur.execute("INSERT INTO Users VALUES (63, '백다연', '수원', '아주대학교', 22, 0062);")
                # cur.execute("INSERT INTO Users VALUES (64, '오채연', '수원', '아주대학교', 21, 0063);")
                # cur.execute("INSERT INTO Users VALUES (65, '왕우진', '성남', '아주대학교', 22, 0064);")
                # cur.execute("INSERT INTO Users VALUES (66, '유다근', '천안', '아주대학교', 24, 0065);")
                # cur.execute("INSERT INTO Users VALUES (67, '이규연', '수원', '아주대학교', 21, 0066);")
                # cur.execute("INSERT INTO Users VALUES (68, '이상훈', '서울', '아주대학교', 24, 0067);")
                # cur.execute("INSERT INTO Users VALUES (69, '이영준', '보령', '아주대학교', 20, 0068);")
                # cur.execute("INSERT INTO Users VALUES (70, '이은채', '오산', '아주대학교', 23, 0069);")
                # cur.execute("INSERT INTO Users VALUES (71, '이준명', '수원', '아주대학교', 23, 0070);")
                # cur.execute("INSERT INTO Users VALUES (72, '전서은', '성남', '아주대학교', 21, 0071);")
                # cur.execute("INSERT INTO Users VALUES (73, '최재영', '진주', '아주대학교', 20, 0072);")
                # cur.execute("INSERT INTO Users VALUES (74, '최준호', '수원', '아주대학교', 24, 0073);")
                # cur.execute("INSERT INTO Users VALUES (75, '정희진', '서울', '아주대학교', 21, 0074);")
                # cur.execute("INSERT INTO Users VALUES (76, '김도형', '수원', '아주대학교', 21, 0075);")
                # cur.execute("INSERT INTO Users VALUES (77, '남현정', '제주', '아주대학교', 21, 0076);")
                # cur.execute("INSERT INTO Users VALUES (78, '문서현', '수원', '아주대학교', 21, 0077);")
                # cur.execute("INSERT INTO Users VALUES (79, '정문영', '천안', '아주대학교', 21, 0078);")
                # cur.execute("INSERT INTO Users VALUES (80, '신수민', '인천', '아주대학교', 23, 0079);")
                # cur.execute("INSERT INTO Users VALUES (81, '나선하', '구미', '아주대학교', 21, 0080);")
                # cur.execute("INSERT INTO Users VALUES (82, '조수희', '광주', '아주대학교', 23, 0081);")
                # cur.execute("INSERT INTO Users VALUES (83, '임진희', '구미', '아주대학교', 20, 0082);")
                # cur.execute("INSERT INTO Users VALUES (84, '송다빈', '구미', '아주대학교', 21, 0083);")
                # cur.execute("INSERT INTO Users VALUES (85, '신민서', '광주', '아주대학교', 22, 0084);")
                # cur.execute("INSERT INTO Users VALUES (86, '김다정', '수원', '아주대학교', 24, 0085);")
                # cur.execute("INSERT INTO Users VALUES (87, '김민아', '수원', '아주대학교', 21, 0086);")
                # cur.execute("INSERT INTO Users VALUES (88, '김선빈', '수원', '아주대학교', 22, 0087);")
                # cur.execute("INSERT INTO Users VALUES (89, '노인산', '장수', '아주대학교', 23, 0088);")
                # cur.execute("INSERT INTO Users VALUES (90, '박단영', '광주', '아주대학교', 21, 0089);")
                # cur.execute("INSERT INTO Users VALUES (91, '이지은', '수원', '아주대학교', 22, 0090);")
                # cur.execute("INSERT INTO Users VALUES (92, '조예린', '수원', '아주대학교', 21, 0091);")
                # cur.execute("INSERT INTO Users VALUES (93, '서동기', '수원', '경희대학교', 20, 0092);")
                # cur.execute("INSERT INTO Users VALUES (94, '김민정', '안양', '아주대학교', 21, 0093);")
                # cur.execute("INSERT INTO Users VALUES (95, '김민영', '서울', '아주대학교', 22, 0094);")
                # cur.execute("INSERT INTO Users VALUES (96, '송희선', '수원', '아주대학교', 20, 0095);")
                # cur.execute("INSERT INTO Users VALUES (97, '박규남', '광주', '아주대학교', 21, 0096);")
                # cur.execute("INSERT INTO Users VALUES (98, '전예지', '화성', '경기대학교', 20, 0097);")
                # cur.execute("INSERT INTO Users VALUES (99, '강나영', '화성', '강남대학교', 20, 0098);")
                # cur.execute("INSERT INTO Users VALUES (100, '변광준', '수원', '아주대학교', 20, 0099);")

            #
            # cur.execute("SELECT * FROM Users;")
            # query = cur.fetchall()
            # for i in query:
            #     print(i)

            # str = ['은', ]
            # # cur.execute("SELECT name FROM Users WHERE name LIKE CONCAT('%', '은' ,'%');")
            # cur.execute("SELECT name FROM Users WHERE name LIKE CONCAT('%', {%s} ,'%');")
            # search_term = '채'

            # query = "SELECT name FROM Users WHERE name LIKE %s;"
            # cur.execute(query, ('%' + search_term + '%',))
            # query = cur.fetchall()
            # for i in query:
            #     print(i)

    except psycopg2.Error as e:
        print("Connection failure.")
        raise e

if __name__ == "__main__":
    user()