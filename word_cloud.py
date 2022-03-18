# 워드 클라우드에 필요한 라이브러리를 불러옵니다.
from wordcloud import WordCloud
# 한국어 자연어 처리 라이브러리를 불러옵니다.
from konlpy.tag import Twitter
# 명사의 출현 빈도를 세는 라이브러리를 불러옵니다.
from collections import Counter
# 그래프 생성에 필요한 라이브러리를 불러옵니다.
import matplotlib.pyplot as plt
# Flask 웹 서버 구축에 필요한 라이브러리를 불러옵니다.
from flask import Flask, request, jsonify

#플라스트 웹 서버 객체를 생성합니다.
app = Flask(__name__)

# 폰트 경로 설정
font_path = 'NanumGothic.ttf'

def get_tag(text, max_count, min_length):
    # 명사만 추출합니다..
    t = Twitter()
    nouns = t.nouns(text)
    processed = [n for n in nouns if len(n) >= min_length]
    # 모든 명사의 출현 빈도를 계산합니다.
    count = Counter(processed)
    result = {}
    # 출현 빈도가 높은 max_count 개의 명사만을 추출합니다.
    for n, c in count.most_common(max_count):
        result[n] = c
    # 추출된 단어가 하나도 없는 경우 '내용이 없습니다.'를 화면에서 보여줍니다.
    if len(result) == 0:
        result["내용이 없습니다."] = 1
    return result
    #