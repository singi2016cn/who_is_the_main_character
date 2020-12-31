'''
分词并过滤后计算单词个数，根据个数正序得到最终结果
'''

from snownlp import SnowNLP
import jieba_filter.water_margin

filterWords = jieba_filter.water_margin.filterWords
roles = {}

with open('data/water_margin.txt', encoding='utf-8') as f:
    content = f.read()
    s = SnowNLP(content)
    words = s.words
    
    for word in words:
        if len(word) <= 1:
            continue
        roles[word] = roles.get(word, 0) + 1
        if word in filterWords:
            del(roles[word])

    items = list(roles.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(6):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))

