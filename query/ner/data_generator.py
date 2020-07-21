import random
import re
import json
import requests
import urllib.parse

ENTITY = '<entity>'
POSITIVE = 'pos'
NEGATIVE = 'neg'

entities = []

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

def get_by_rule(file,num):

    with open(file,'r',encoding="utf-8") as reader:
        for line in reader:
            line = line.strip()
            line = line.replace("<entity>","wenwu_name")


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
    write(positive, negative, '../../data/caizhi.txt', '../../data/chaodai-other.txt')
    # positive, negative = load_rule_instance()
    # extend_from_file(positive, negative)
    # write(positive, negative, 'data/set/abstract.txt', 'data/set/other.txt')
    # entities.append('周杰伦')
    # positive, negative = gen_by_rule(10)
    # for line in positive:
    #     print(line)

