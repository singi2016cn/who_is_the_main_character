import pandas as pd
import re

'''
主程序，根据配置匹配特定单词出现次数
'''


def count_words(input_file, config, is_out_csv=False, output_file=''):
    with open(input_file, 'r', encoding='utf-8') as f:
        title = config.title
        chapter_filter_pattern = config.chapter_filter_pattern
        chapter_name = config.chapter_name
        roles = config.roles

        chapter_number = 0
        chapter_arr = []
        pdcsv = {}

        main_character_count = 0
        main_character = ''

        while True:
            line = f.readline()

            if re.search(chapter_filter_pattern, line) is not None or line == '':
                chapter_number += 1
                if chapter_number == 1:
                    continue
                chapter = get_chapter(chapter_number - 1)
                chapter_arr.append(chapter)
                for role in roles:
                    role['chapterCount'].append(role['totalCount'])
                if line == '':
                    break

            for role in roles:
                if not role.__contains__('chapterCount'):
                    role.setdefault('chapterCount', [])
                if not role.__contains__('totalCount'):
                    role.setdefault('totalCount', 0)
                count = count_with_arr(line, role['filter_words'])
                role['totalCount'] += count

        print('%s谁才是主角？' % title)

        pdcsv[chapter_name] = chapter_arr
        for role in roles:
            name = role['filter_words'][0]
            print('%s总出场次数：%s' % (name, role['totalCount']))
            pdcsv[name] = role['chapterCount']
            if main_character_count < role['totalCount']:
                main_character_count = role['totalCount']
                main_character = name

        print('主角是%s!!!' % main_character)

    if is_out_csv:
        # 生成动态条形图csv
        dataframe = pd.DataFrame(pdcsv)
        dataframe.to_csv(output_file, index=False, sep=',')


'''
计算给定的数组中字符出现的总次数
'''


def count_with_arr(content, filter_words):
    count = 0
    for words in filter_words:
        count += content.count(words)
    return count


'''
数字转汉字
'''


def number2words(number, recursive_depth=0):
    str_number = str(number)
    if len(str_number) > 4:
        str_number = str_number[-4:]
    bits = "零 一 二 三 四 五 六 七 八 九".split(" ")
    units = " 十 百 千".split(" ")
    large_unit = ' 万 亿 万'.split(" ")  # 可扩展,以万为单位
    number_len = len(str_number)
    result = ""

    for i in range(number_len):
        result += bits[int(str_number[i])]
        if str_number[i] != "0":
            result += units[number_len - i - 1]

    # 去除连续的零
    while "零零" in result:
        result = result.replace("零零", "零")
    # 去除尾部的零
    if result[-1] == "零":
        result = result[:-1]
    # 调整10~20之间的数
    if result[:2] == "一十":
        result = result[1:]
    # 字符串连接上大单位
    result += large_unit[recursive_depth]

    # 判断是否递归
    if len(str(number)) > 4:
        recursive_depth += 1
        return number2words(str(number)[:-4], recursive_depth) + result
    else:
        return result


def get_chapter(chapter_number):
    return '第' + number2words(chapter_number) + '回'
