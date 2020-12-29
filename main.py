import tools
import config
import pandas as pd

with open('data/the_three_kingdoms.txt', 'r', encoding='utf-8') as f:
    roles = config.roles

    initChapterIndex = 1
    chapterNumber = 0
    csv = []
    tmp = []
    chapterArr = []
    pdcsv = {}

    while(True):
        line = f.readline()

        if (line.find('正文') > -1 or line == ''):
            chapterNumber += 1
            if chapterNumber == 1:
                continue
            chapter = tools.getChapter(chapterNumber - 1)
            chapterArr.append(chapter)
            for role in roles:
                role['chapters'].append(role['totalCount'])
            if line == '':
                break

        for role in roles:
            count = tools.countWithArr(line, role['filterWords'])
            role['totalCount'] += count
        
    
    print('三国演义谁才是主角？')

    pdcsv['章节'] = chapterArr
    for role in roles:
        print('%s总出场次数：%s' % (role['name'], role['totalCount']))
        pdcsv[role['name']] = role['chapters']


# 生成动态条形图csv
dataframe = pd.DataFrame(pdcsv)
dataframe.to_csv("output/the_three_kingdoms.csv",index=False,sep=',')