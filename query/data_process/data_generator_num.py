import random
import re
import json
import requests
import urllib.parse

ENTITY = '<entity>'
POSITIVE = 'pos'
NEGATIVE = 'neg'

entities = []
value = []

PREFIX_ASK = ['', '', '', '请问', '你知道', '请问', '你知道', '请问', '你知道', '请问你知道', '你说', '我问你', '我问问你', '我考考你', '考考你', '我考一考你', '考一考你', '告诉我', '请告诉我', '请你告诉我', '回答我', '请回答我', '请你回答我', '我想知道']
PLEASE_DO = ['', '请', '请你', '', '请', '请你', '你能', '你会', '你可以', '能不能', '可不可以']
PREFIX_DO = ['', '', '', '', '', '给我', '给我', '给我', '给我', '给我们', '为我', '为我们', '帮我', '帮我们', '向我', '向我们']
DO = ['', '', '', '讲讲', '说说', '讲下', '说下', '讲一讲', '说一说', '讲一下', '说一下', '回答', '所搜',  '查一下', '搜一下', '查', '搜']
SUFFIX = ['', '', '', '', '', '', '', '', '', '', '', '', '么', '吗', '嘛']
SUFFIX_ = ['么',  '行不行', '好不好','好吗',  '可以吗', '好不', '行吗', '行不']
key = ['朝代', '材质','用途','纹饰', '寓意', '体积', '文化', '工艺','窑口']
# yuyi_value_list = ["吉祥", "喜庆", "如意", "富贵", "平安", "庄严", "庄重", "春节", "福寿", "简单", "美好", "高雅", "祥瑞", "神圣"]
# chaodai_value_list =  ["宋朝", "宋代", "宋时期", "清朝", "清代", "清朝时期", "唐朝", "唐代", "汉朝",  "汉代", "元朝","商朝","明朝","明代","三国时期","战国","春秋","新石器时代","晋朝"]
# caizhi_value_list = ["漆器","玉器","玻璃器","珐琅","金银锡器","陶瓷","青铜器"]
# yongtu_value_list = ["乐器","兵器","水器","度量衡","烹饪器","生活用具","车马器","酒器","陈设器"]
# gongyi_value_list = ["彩绘","剔红","釉下彩","雕塑","镶嵌","珐琅彩","珍珠地","颜色釉","剔彩","剔花"]
# wenshi_value_list = ["鱼纹","莲瓣纹","水波纹","弦纹","龙纹","菊花纹"]
# category_value_list = ["碗","杯","瓶","壶","盒","盘"]
# value.extend(caizhi_value_list)
# value.extend(yuyi_value_list)
# value.extend(chaodai_value_list)
# value.extend(yongtu_value_list)
# value.extend(gongyi_value_list)
# value.extend(wenshi_value_list)
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
        pos = ENTITY
        mode = random.random()
        if mode <= 0.1:
            part_b = ''
            part_a = ''
        elif mode <= 0.5:
            # 纹饰为xx的文物有多少
            mode2 = random.randint(0, 5)
            if mode2 == 1:
                part_b = random.choice(PREFIX_ASK)
            elif mode2 == 2:
                part_b = random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 4:
                part_b = random.choice(PREFIX_DO) + random.choice(DO)
            elif mode2 == 5:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO) + random.choice(DO)
            part_a = random.choice(['文物数量', '']) + \
                     random.choice(['有', '有', '有', '占', '含有', '包含', '存在', '包括']) + random.choice(
                ['多少', '多少', '多少', '多少', '多些', '几多', '多少']) + random.choice(SUFFIX)
            pos = part_b + random.choice(key) + "为" + ENTITY  + part_a

        elif mode <= 1.0:
            #
            mode2 = random.randint(0, 5)
            if mode2 == 1:
                part_b = random.choice(PREFIX_ASK)
            elif mode2 == 2:
                part_b = random.choice(DO)
            elif mode2 == 3:
                part_b = random.choice(PLEASE_DO) + random.choice(DO)
            elif mode2 == 4:
                part_b = random.choice(PREFIX_DO) + random.choice(DO)
            elif mode2 == 5:
                part_b = random.choice(PLEASE_DO) + random.choice(PREFIX_DO) + random.choice(DO)
            part_a = random.choice(['文物数量', '']) + \
                     random.choice(['有', '有', '有', '占', '含有', '包含', '存在', '包括']) + random.choice(
                ['多少', '多少', '多少', '多少', '多些', '几多', '多少']) + random.choice(SUFFIX)
            pos = part_b + ENTITY + part_a

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

    positive, negative = gen_by_rule(2000)
    write(positive, negative, '../../data/num.txt', '../../data/chaodai-other.txt')
    # positive, negative = load_rule_instance()
    # extend_from_file(positive, negative)
    # write(positive, negative, 'data/set/abstract.txt', 'data/set/other.txt')
    # entities.append('周杰伦')
    # positive, negative = gen_by_rule(10)
    # for line in positive:
    #     print(line)

