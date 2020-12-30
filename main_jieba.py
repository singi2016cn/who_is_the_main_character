import jieba

roles = {}
with open('data/the_three_kingdoms.txt', encoding='utf-8') as f:
    content = f.read()
    words = jieba.lcut(content)
    
    for word in words:
        if len(word) <= 1:
            continue
        roles[word] = roles.get(word, 0) + 1

    items = list(roles.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(50):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))


    