'''
from comtypes.automation import _
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugsmusic:

    url = ''

    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'lxml')
        cnt_artist = 0
        cnt_title = 0

        '''
        for link1 in soup.find_all(name='p', attrs=({"class" : "artist"})):
            cnt_artist += 1
            print(str(cnt_artist) + "위")
            print("아티스트 : " + link1.find('a').text)

        print("-------------------------------------------")

        for link2 in soup.find_all(name='p', attrs=({"class" : "title"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("제목 : " + link2.text.replace("\n",""))
        '''

        for link3 in soup.find_all(name='tr', attrs=({"rowtype": "track"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("제목 : " + link3.find(name='p', attrs=({"class": "title"})).text.replace("\n", ""))
            print("아티스트 : " + link3.find(name='p', attrs=({"class": "artist"})).text.replace("\n", ""))
            print("-------------------------------------------")

    @staticmethod
    def main():
        date = "20210508"
        bugs = Bugsmusic()
        bugs.url = f"https://music.bugs.co.kr/chart/track/realtime/total?chartdate={date}&charthour=10"
        bugs.scrap()

if __name__ == '__main__':
    Bugsmusic.main()