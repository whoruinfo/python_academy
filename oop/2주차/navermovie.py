from selenium import webdriver
from bs4 import BeautifulSoup

class Navermovie(object) :

    chromedriver = "C:\Program Files\Google\Chrome\chromedriver"
    url = ""

    def scrap(self):
        driver = webdriver.Chrome(self.chromedriver)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class": "tit3"})

        for i in [div.a.string for div in all_div]:
            print(i)
        driver.close()


    @staticmethod
    def main():
        movie = Navermovie()
        movie.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        movie.scrap()

if __name__ == '__main__':
    Navermovie.main()