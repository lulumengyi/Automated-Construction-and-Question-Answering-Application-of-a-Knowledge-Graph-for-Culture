import random
import re
import json
import requests
import urllib.parse


ENTITY = '<entity>'
POSITIVE = 'pos'
NEGATIVE = 'neg'

entities = []

PREFIX_ASK = ['', '', '', '请问', '你知道', '请问', '你知道', '请问', '你知道', '请问你知道', '你说', '我问你', '我问问你', '我考考你', '考考你', '我考一考你', '考一考你', '告诉我', '请告诉我', '请你告诉我', '回答我', '请回答我', '请你回答我', '我想知道']
PLEASE_DO = ['', '请', '请你', '', '请', '请你', '你能', '你会', '你可以', '能不能', '可不可以']
PREFIX_DO = ['', '', '', '', '', '给我', '给我', '给我', '给我', '给我们', '为我', '为我们', '帮我', '帮我们', '向我', '向我们']
DO = ['', '', '', '讲讲', '说说', '讲下', '说下', '讲一讲', '说一说', '讲一下', '说一下', '回答', '所搜',  '查一下', '搜一下', '查', '搜']
SUFFIX = ['', '', '', '', '', '', '', '', '', '', '', '', '么', '吗', '嘛']
SUFFIX_ = ['么',  '行不行', '好不好','好吗',  '可以吗', '好不', '行吗', '行不']


# user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# headers = {'User_Agent': user_agent}
# sessions = requests.session()
# sessions.headers = headers
# url = 'http://172.16.10.10:23000'
# headers = {'content-type': 'application/json'}
# d = json.dumps({'query': '周杰伦'})
# response = requests.post(url, data=d, headers=headers)
# result = urllib.parse.unquote(response.text)
# print('entity linker test done')




def gen_by_rule(num):
    positive = []
    negative = []
    for i in range(num):
        #entity = random.choice(entities)
        part_b = ''
        part_a = ''
        mode = random.random()
        if mode <= 0.1:
            part_b = ''
            part_a = ''
        elif mode <= 0.35:
            mode2 = random.randint(0, 5)
            if mode2 == 1:
                part_b = random.choice(PREFIX_ASK)
                part_c =  random.choice(SUFFIX)
            elif mode2 == 2:
                part_b = random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 4:
                part_b = random.choice(PREFIX_DO) + random.choice(DO)
            elif mode2 == 5:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO) + random.choice(DO)
            part_a = random.choice(['出土于', '属于', '归属于', '是','为', '归为', '产生于', '是']) + random.choice(['什么', '哪个']) + random.choice(['朝代', '年代','时代', '时期','时间', '阶段'])
            part_c = random.choice(SUFFIX_)
        elif mode <= 0.6:
            mode2 = random.randint(0, 5)
            if mode2 == 1:
                part_b = random.choice(PREFIX_ASK)
                part_c = random.choice(SUFFIX)
            elif mode2 == 2:
                part_b = random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 4:
                part_b = random.choice(PREFIX_DO) + random.choice(DO)
            elif mode2 == 5:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO) + random.choice(DO)
            part_a =  random.choice(['的', ''])  + random.choice(['朝代', '年代', '时代', '时期', '时间', '阶段']) + random.choice(['属于', '归属于', '是', '为', '归为', '产生于', '是'])+ random.choice(['什么时候', '何时', '什么时间', '几时', '哪时'])
            part_c = random.choice(SUFFIX_)
        elif mode <= 0.8:
            mode2 = random.randint(0, 5)
            if mode2 == 1:
                part_b = random.choice(PREFIX_ASK)
                part_c = random.choice(SUFFIX)
            elif mode2 == 2:
                part_b = random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 4:
                part_b = random.choice(PREFIX_DO) + random.choice(DO)
            elif mode2 == 5:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO) + random.choice(DO)
            part_a =  random.choice(
                ['属于', '归属于', '是', '为', '归为', '产生于', '是']) + random.choice(
                ['什么时候', '何时', '什么时间', '几时', '哪时'])
            part_c = random.choice(SUFFIX_)

        elif mode <= 0.9:
            mode2 = random.randint(0, 3)
            if mode2 == 1:
                part_b = random.choice(PREFIX_DO)+ random.choice(DO)
            elif mode2 == 2:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO)
            part_a =  random.choice(['的', '']) + random.choice(['朝代', '年代', '时代', '时期', '时间', '阶段'])  + random.choice(
                ['什么时候', '何时', '什么时间', '几时', '哪时'])
            part_c = random.choice(SUFFIX_)

        else:
            mode2 = random.randint(0, 3)
            if mode2 == 1:
                part_b = random.choice(PREFIX_DO)
            elif mode2 == 2:
                part_b = random.choice(PLEASE_DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO)
            part_b += random.choice(['介绍', '简介', '介绍', '简介', '介绍', '简介', '简单介绍', '百度', '百科', '百度百科']) + random.choice(['', '一下'])
            part_a = random.choice(['的', '']) + random.choice(['朝代', '年代', '时代', '时期', '时间', '阶段']) + "是"+random.choice(
                ['什么时候', '何时', '什么时间', '几时', '哪时'])
            part_c = random.choice(SUFFIX_)


        pos = part_b + ENTITY + part_a +part_c
        if pos != ENTITY and part_a != '':
            positive.append(pos)

        print('\rgenerate:', i, end='')
    print('\rgenerate:', len(positive) + len(negative), end='\n')
    return positive, negative



def write(positive, negative, pos_file, neg_file):
    print('writing.................')
    with open(pos_file, 'w', encoding='utf8') as writer:
        for query in positive:
            writer.write(query + '\n')
    with open(neg_file, 'w', encoding='utf8') as writer:
        for query in negative:
            writer.write(query + '\n')
    print('positive:', len(positive), 'negative:', len(negative))


if __name__ == '__main__':

    positive, negative = gen_by_rule(2500)
    write(positive, negative, '../../data/chaodai.txt', '../../data/chaodai-other.txt')
    # positive, negative = load_rule_instance()
    # extend_from_file(positive, negative)
    # write(positive, negative, 'data/set/abstract.txt', 'data/set/other.txt')
    # entities.append('周杰伦')
    # positive, negative = gen_by_rule(10)
    # for line in positive:
    #     print(line)

