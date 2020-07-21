import jieba

def get_wenwu_list(file1,file2):
    wenwu_list = []
    with open(file1,'r',encoding="utf-8") as reader:
        with open(file2,'w',encoding="utf-8") as writer:
            for line in reader:
                data = line.strip().split("\t")
                if data[0] not in wenwu_list:
                    wenwu_list.append(data[0])
            for wenwu in wenwu_list:
                writer.write(wenwu+"\n")
    return wenwu_list

#get_wenwu_list(r"C:\Users\lumengyi\DouBan\WenWu_KGQA\data\process_data\triples.txt",r"C:\Users\lumengyi\DouBan\WenWu_KGQA\query\ner\wenwu.txt")

def get_by_rule(file1,file2,file3):
    wenwu_list = []
    with open(file1, 'r', encoding="utf-8") as reader:
        for line in reader:
            line = line.strip()
            wenwu_list.append(line)

    with open(file2, 'r', encoding="utf-8") as reader:
        with open(file3,'w',encoding="utf-8") as writer:
            i = 0
            for line in reader:
                line = line.strip()
                try:
                    data = line.split("<entity>")
                    pre_data = list(data[0])
                    post_data = list(data[-1])
                    for char in pre_data:
                        writer.write(char+"\t" + "O"+"\n")
                    writer.write(list(wenwu_list[i])[0] + "\t" + "B-RELIC" + "\n")
                    for j in range(1,len(list(wenwu_list[i]))-1):
                        writer.write(list(wenwu_list[i])[j] + "\t" + "I-RELIC" + "\n")
                    writer.write(list(wenwu_list[i])[-1] + "\t" + "O-RELIC" + "\n")
                    for char in post_data:
                        writer.write(char+"\t" + "O"+"\n")
                    writer.write("\n")
                except:
                    i = 0
                i += 1

get_by_rule("data/wenwu.txt","data/test.txt","data/output.txt")