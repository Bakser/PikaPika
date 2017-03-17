import pymysql

class WikiSearcher:
    def __init__(self):
        self.connection= pymysql.connect(host='localhost',user='root',db ='wikidb',charset='utf8')
        self.cursor = self.connection.cursor()

    def exist(self,title):
        self.cursor.execute("SELECT * FROM MAIN WHERE title=%s",(title))
        return self.cursor.fetchone() != None

    def __del__(self):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    WS = WikiSearcher()
    WS.exist("欧洲")
