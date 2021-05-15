from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SamsungReport(object):

    def __init__(self):
        self.okt = Okt(jvmpath='C:\\Program Files\\Java\\jdk1.8.0_281\\jre\\bin\\server\\jvm.dll')

    def read_file(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = './data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()

        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n','')#개행 치환
        tokenizer = re.compile(r'[^ ㄱ-힣]+')# 한글의  단어별로 분리
        temp = tokenizer.sub('', temp)
        return temp

    #  문장에서 단어를 토큰화 시킨다.
    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
        return tokens

    # 명사를 추출  konlpy 에 딕셔너리를 이용하여 가져옴
    def extract_noun(self):
        noun_tokens = []
        tokens = self.change_token(self.extract_hangeul(self.read_file()))

        for token in tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))

            texts = " ".join(noun_tokens)
            return texts

    @staticmethod
    def download():
        nltk.download()

    @staticmethod
    def read_stopword():
        stopfile = './data/stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        return stopwords

    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
        stopwords = self.read_stopword()
        #stop word 파일에 없는 단어만 담는다.
        texts = [text for text in tokens if text not in stopwords]
        return texts

    def hook(self):
        texts = self.read_stopword()
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        print(freqtxt[:30])
        return freqtxt

    def draw_wordcloud(self):
        texts = self.read_stopword()
        wcloud = WordCloud('./data/D2Coding.ttf', relative_scaling=0.2,
                           background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    @staticmethod
    def main():
        samsung = SamsungReport()
        samsung.hook()
        samsung.draw_wordcloud()

if __name__ == '__main__':
    SamsungReport.main()