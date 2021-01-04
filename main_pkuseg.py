"""
分词并过滤后计算单词个数，根据个数正序得到最终结果

n   名词    t   时间词  s   处所词  f   方位词  m   数词
q   量词    b   区别词  r   代词    v   动词    a   形容词
z   状态词  d   副词    p   介词    c   连词    u   助词
y   语气词  e   叹词    o   拟声词  i   成语    l   习惯用语
j   简称    h   前接成分    k   后接成分    g   语素    
x   非语素字    w   标点符号    nr  人名    ns  地名
nt  机构名称    nx  外文字符    nz  其它专名    vd  副动词
vn  名动词  vx  形式动词    ad  副形词  an  名形词
"""

import pkuseg

roles = {}

with open('data/the_dream_of_red_mansion.txt', encoding='utf-8') as f:
    content = f.read()
    seg = pkuseg.pkuseg(model_name='medicine', postag=True)
    words = seg.cut(content)

    for word in words:
        if len(word) <= 1:
            continue
        if word[1] in ['n', 'nr']:
            roles[word[0]] = roles.get(word[0], 0) + 1

    items = list(roles.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(items)):
        word, count = items[i]
        if count > 100:
            print('{0:<10}{1:>5}'.format(word, count))
