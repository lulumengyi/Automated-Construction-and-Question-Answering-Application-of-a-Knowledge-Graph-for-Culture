import json
import jieba

#把关键词添加到jieba分词的自定义词典中，防止被切开
def add_keyword_to_userdict(rfile,wfile):
    exsit_words = []
    with open(rfile,'r',encoding="utf-8") as reader:
        with open(wfile,'w',encoding="utf-8") as writer:
            for line in reader:
                record = json.loads(line.strip())
                keywords = record["keyword"]
                for word in keywords:
                    writer.write(word+"\n")

# jieba.load_userdict("data/jieba_userdict.txt")
# #加载停用词表
# stop = [line.strip() for line in open('data/stopwords.txt',encoding="utf-8").readlines()]

# 对爬取下来的json文件，进行属性完善,纹饰类这我也只是做了简单的例子，也可完善下abstract中出现过的纹饰。其他属性提取方法可不同，多思考下，比如功能用途
def add_property_to_jsonfile(rfile,wfile):
    featureWords = {}
    # 将整理好的本体文件，读取成字典
    with open("data/feature.txt",'r',encoding="utf-8") as reader:
        for line in reader:
            data = line.strip().split("\t")
            category = data[0]
            word = data[1]
            if word not in featureWords:
                featureWords[word] = category
    # 增加属性
    with open(rfile,'r',encoding="utf-8") as reader:
        with open(wfile,'w',encoding="utf-8") as writer:
            for line in reader:
                newrecord = {}
                record = json.loads(line.strip())
                name = record["title"]
                newrecord["中文名"] = name
                newrecord["朝代"] = record["period"]
                if record["category"] != "":
                    newrecord["类型"] = record["category"]
                if record["yaokou"] != "":
                    newrecord["窑口"] = record["yaokou"]
                abstract = record["abstract"]
                keywords = record["keyword"]
                for word in keywords:
                    if "纹" in word:
                        newrecord["纹饰"] = word
                seg_list = jieba.cut(abstract)
                for word in seg_list:
                    if word not in stop:
                        if word in featureWords:
                            category = featureWords[word]
                            newrecord[category] = word
                jsonstr = json.dumps(newrecord, ensure_ascii=False)
                writer.write(jsonstr + '\n')


# 将把property已经完善好的json文件转换为三元组格式
def get_triple_file(rfile,wfile):
    with open(rfile,'r',encoding="utf-8") as reader:
        with open(wfile,'w',encoding="utf-8") as writer:
            for line in reader:
                try:
                    record = json.loads(line.strip())
                except:
                    print(line)
                title = record["中文名"]
                name = "<http://kg.BLCU.edu/entity/" + title +">"
                property_prefix = "<http://kg.BLCU.edu/ontology/property/"
                for key,value in record.items():
                    if key != title:
                        if key == "纹饰":
                            for item in value:
                                property_name = property_prefix + key + ">"
                                item = '"' + item + '"'
                                writer.write(name + " " + property_name + " " + str(item) + " " + "." + "\n")
                        else:
                            property_name = property_prefix + key + ">"
                            value = '"' + value + '"'
                            writer.write(name + " " + property_name + " " + str(value) + " " + "." +"\n")

#add_property_to_jsonfile("data/ceramics.json","data/wenwu.json")
#get_triple_file("data/wenwu.json","data/dictionary.nt")
#get_triple_file("data/wenwu_.json","data/rdf/wenwu_kgqa.nt")
#add_keyword_to_userdict("data/ceramics.json","data/jieba_userdict.txt")

import json


def add_keyword_to_userdict(rfile, wfile):
    exsit_words = []
    count = 0
    with open(rfile, 'r', encoding="utf-8") as reader:
        with open(wfile, 'w', encoding="utf-8") as writer:
            for line in reader:
                record = json.loads(line.strip())
                title = record["中文名"]
                writer.write(title +"\t"+"nz"+ "\n")
                # try:
                #     chaodai = record["朝代"]
                #     # writer.write(chaodai+ "\n")
                # except:
                #     count += 1
                #     print(title)
                # try:
                #     yaokou = record["窑口"]
                #     writer.write(yaokou +"\t"+"n"+ "\n")
                # except:
                #     pass
                # try:
                #     xingzhuang = record["形状"]
                #     writer.write(xingzhuang +"\t"+"n"+ "\n")
                # except:
                #     pass
                # try:
                #     gongyi = record["工艺"]
                #     writer.write(gongyi +"\t"+"n"+ "\n")
                # except:
                #     pass
                # try:
                #     caizhi = record["材质"]
                #     writer.write(caizhi +"\t"+"n"+ "\n")
                # except:
                #     pass
                # try:
                #     wenshi = record["纹饰"]
                #     for item in wenshi:
                #         writer.write(item +"\t"+"n"+ "\n")
                # except:
                #     pass
            print(count)


add_keyword_to_userdict("data/wenwu_.json", "data/jieba_userdict.txt")