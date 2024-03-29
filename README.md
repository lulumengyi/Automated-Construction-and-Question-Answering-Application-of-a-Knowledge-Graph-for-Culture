
# 文物知识图谱的自动化构建及问答应用

## 任务一 爬取数据
1. 数据源

本次调研到如下的网站可进行抽取数据
 - 故宫博物院 https://www.dpm.org.cn/collection/ceramics.html
 - 百度博物馆计划 https://baike.baidu.com/museum/
 - 国家文物局 http://www.sach.gov.cn/index.html 
 - 历史千年  http://www.lsqn.cn/Index.html （历史名人、历史故事）
 - 中国历代人物传记资料库 http://db1.ihp.sinica.edu.tw/cbdbc/ttsweb?@0:0:1:cbdbkm@@0.47946741292253137 
 - 北京大学中国古代史研究中心 https://zggds.pku.edu.cn/slxx/58709.htm

数据处理流程：
![img/1371701677788_.pic.jpg](https://github.com/lulumengyi/Automated-Construction-and-Question-Answering-Application-of-a-Knowledge-Graph-for-Culture/blob/master/img/1371701677788_.pic.jpg)
 
 ## 任务二 知识图谱构建
 目前考虑到的实体
 - 藏品
 
 | 名称 | 所属年代 | 出土时间 | 出土地点 | 馆藏地点 |简介 |类别|
| -------- | ---- | ---- | -------- | ----------- | ----------| ----------|
| 三羊铜罍   | 商早期（公元前16世纪——前14世纪）   | 不详   | 平谷刘家河   | 首都博物馆 |..|青铜器|
| 原始青瓷豆    | 西周（前1046-前771）   | 1974年   | 北京房山区琉璃河乡商周遗址52号墓   |  首都博物馆 |  ... | 陶瓷器|

 - 博物馆
 
  | 名称 | 地点 | 开发时间 | 成立时间 | 所属国家|所属城市|门票价格|总建筑面积|现任馆长|馆藏精品|类别|
  | -------- | ---- | ---- | -------- | ----------- | ----------| -------| --------|-----|---|---|
  |...|...|...|..|..|...|..|..|..|..|..|
 - 建筑
 
  | 名称 | 地理位置 | 建造时间 |简介|类别|
  | --| ---- | ---- | -----|-- | 
  | 坤宁门| 坤宁宫 | 明代初期| -----|宫廷建筑 | 
 - 人物
 
 | 名称 | 别名 | 出生时间 | 所属年代 | 类别|
| -------- | ---- | ---- | -------- | --|
| -------- | ---- | ---- | -------- | 历史人物|
| -------- | ---- | ---- | -------- | 学术专家|
 
 ## 任务三 将数据存入知识图谱数据库
 
 |编号|	名称|	主要功能|
 | --| ---- | ---- |
|1	|Neo4j	|开源图形数据库，由Java开发。|
|2	|OrientDB	|开源的noSQL数据库，可处理文档、图形、传统数据库组件。由Java编写，存储速度快。|
|3	|Virtuoso	|支持RDF与SPARQL查询。|
|4	|Titan	|可与Gremlin/Hbase进行集成，可实现分布式存储和计算的图数据处理。|
|5	|Apache Jena-IDB|	在JAVA下操作RDF。其中TDB是使用triple store的形式对RDF数据提供持久性存储（persistent store），TDB相比RDB、SDB更快且具有扩展性。|
|6	|Cypher|	声明式图查询语言，表达高效查询和更新图数据库。|
|7	|Gremlin|	一种函数式数据流语言，可以使得用户使用简洁的方式表述复杂的属性图（property graph）的遍历或查询。|
|8	|SPARQL|	为RDF开发的一种查询语言和数据获取协议。|
|9	|rdflib|	基于Python语言编写的，RDF / XML，N3，NTriples，N-Quads，Turtle，TriX，RDFa和Microdata的解析器和序列化器，支持SPARQL 1.1查询和更新语句。|

#### Neo4j

1. 创建可以导⼊Neo4j的csv文件

生成csv格式，参考https://neo4j.com/docs/operations-manual/current/tutorial/import-tool/

2. 利用上面的csv文件生成数据库
```
neo4j_home$ bin/neo4j-admin import --nodes executive.csv --nodes stock.csv -- nodes concept.csv --nodes industry.csv --relationships executive_stock.csv --relationships stock_industry.csv -- relationships stock_concept.csv
```
#### SPARQL

将数据整理成.nt格式
```
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/Category> "人物" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/Category> "影视人物" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/中文名> "李荣浩" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/外文名> "Youngho Lee，Ronghao Li" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/国籍> "中国" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/民族> "回族" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/星座> "巨蟹座" .
<http://kg.soundai.com/entity/李荣浩> <http://kg.soundai.com/ontology/property/身高> "180cm" .
```
## 任务四 问答数据集构建
```
1. 首都博物馆共有多少件藏品？
2. 彩绘陶马是什么年代的文物？
3. 故宫博物馆什么时候开放？

```
 
 ## 任务四 实体链接词典构建
 
 从问句中提取出实体可以采用以下两种方法：1）构建诸如BiLSTM-CRF(https://arxiv.org/pdf/1508.01991.pdf)等深度学习模型，然后利用训练好的深度学习模型预测出问句实体。2）构建实体词表，从问句中提取词表中所包含的实体。
 
 ## 任务五 关系链接算法
 
关系链接可以采用以下两种方法：1）构建诸如CNN等多分类深度学习模型，然后利用训练好的深度学习模型预测问句的目标属性。2）构建关键词集合，把问句中所包含的关键词当作问句的目标属性。
 
 ## 任务六 SPARQL知识检索/通过编写Cypher语句回答问题
 
 ## 任务七 可视化平台搭建

 
 

