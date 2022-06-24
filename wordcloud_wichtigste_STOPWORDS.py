from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("test_wordcloud.txt") as f:
    text = f.read()

wordcloud = WordCloud(width=1920, height=1200)

STOPWORDS.add('der')
STOPWORDS.add('die')
STOPWORDS.add('das')
STOPWORDS.add('und')
STOPWORDS.add('in')
STOPWORDS.add('zu')
STOPWORDS.add('ein')
STOPWORDS.add('eine')
STOPWORDS.add('von')
STOPWORDS.add('Sie')
STOPWORDS.add('vom')
STOPWORDS.add('den')
STOPWORDS.add('oder')
STOPWORDS.add('sich')
STOPWORDS.add('des')
STOPWORDS.add('zum')
STOPWORDS.add('werden')
STOPWORDS.add('wir')
STOPWORDS.add('ihr')
STOPWORDS.add('ist')
STOPWORDS.add('nicht')
STOPWORDS.add('für')
STOPWORDS.add('mit')
STOPWORDS.add('bei')
STOPWORDS.add('einer')
STOPWORDS.add('sind')
STOPWORDS.add('kann')
STOPWORDS.add('im')
STOPWORDS.add('Welche')
STOPWORDS.add('auf')
STOPWORDS.add('wird')
STOPWORDS.add('auch')
STOPWORDS.add('als')
STOPWORDS.add('nach')
STOPWORDS.add('dass')
STOPWORDS.add('es')
STOPWORDS.add('hat')
STOPWORDS.add('einen')
STOPWORDS.add('er')
STOPWORDS.add('wenn')
STOPWORDS.add('dem')
STOPWORDS.add('wie')
STOPWORDS.add('einem')
STOPWORDS.add('eines')
STOPWORDS.add('aus')
STOPWORDS.add('durch')
STOPWORDS.add('vor')
STOPWORDS.add('Warum')
STOPWORDS.add('diese')
STOPWORDS.add('muss')
STOPWORDS.add('nur')
STOPWORDS.add('können')
STOPWORDS.add('haben')
STOPWORDS.add('über')
STOPWORDS.add('zwischen')
STOPWORDS.add('mehr')
STOPWORDS.add('unter')

wordcloud.generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()