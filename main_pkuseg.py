"""
分词并过滤后计算单词个数，根据个数正序得到最终结果
"""

import pkuseg
import jieba_filter.water_margin

filter_words = jieba_filter.water_margin.filter_words
roles = {}

with open('data/the_dream_of_red_mansion.txt', encoding='utf-8') as f:
    content = f.read()
    seg = pkuseg.pkuseg(model_name='medicine')
    words = seg.cut(content)

    for word in words:
        if len(word) <= 1:
            continue
        roles[word] = roles.get(word, 0) + 1
        if word in filter_words:
            del (roles[word])

    items = list(roles.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(100):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))
