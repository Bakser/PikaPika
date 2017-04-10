import pymysql
import wikipedia
import sys
sys.path.append('.')
import langconv

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

class WikiSearcher_online:
    def __init__(self):
        wikipedia.set_lang('zh')

    def exist(self,tt):
        try:
            wikipedia.page(title=tt)
        except wikipedia.exceptions.PageError as e:
            return False
        except wikipedia.exceptions.DisambiguationError:
            return False
        else:
            return True

    def get_links(self,tt):
        try:
            lst = wikipedia.page(title=tt).links
            return [langconv.Converter('zh-hans').convert(w) for w in lst]
        except wikipedia.exceptions.PageError as e:
            return []
        except wikipedia.exceptions.DisambiguationError as e:
            return []


if __name__ == '__main__':
    WS = WikiSearcher_online()
    print(WS.get_links("欧洲"))
