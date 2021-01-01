'''
分词并过滤后计算单词个数，根据个数正序得到最终结果
'''

import jieba
import jieba_filter.water_margin

filter_words = jieba_filter.water_margin.filter_words
roles = {}

with open('data/water_margin.txt', encoding='utf-8') as f:
    content = f.read()
    words = jieba.lcut(content)
    
    for word in words:
        if len(word) <= 1:
            continue
        roles[word] = roles.get(word, 0) + 1
        if word in filter_words:
            del(roles[word])

    items = list(roles.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(6):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))
