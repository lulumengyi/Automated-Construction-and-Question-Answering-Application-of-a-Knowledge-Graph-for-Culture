# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
书籍信息
"""
from refo import Star, Any
from inference.basic_inference import W, Rule, KeywordRule
from inference.basic_inference import SPARQL_PREFIX, SPARQL_ASK_TEM, SPARQL_COUNT_TEM, SPARQL_SELECT_TEM
from inference.basic_inference import pos_wenwu, pos_other, pos_number, wenwu_entity, other_entity, number_entity
from inference.basic_inference import WenwuPropertyValueSet

chaodai = W("朝代") | W("朝") | W("代")# 朝代
category = (W("类型") | W("种类") | W('类别')| W('什么类'))  # 类型
wenshi = (W("纹饰") | W("花纹") )  # 纹饰
gongyi = (W("工艺") | W("制作手段") | W('怎么制作'))  # 类型
yuyi = (W("寓意") | W("含义"))  # 类型
yaokou = (W("窑口") | W("窑") )  # 类型
gao = (W("高") | W("多高"))  # 类型
zujing= (W("足径"))  # 类型
koujing =  (W("口径"))
caizhi = (W("材质"))  # 类型
xingzhuang = (W("形状"))  # 类型
yongtu = (W("用途"))  # 类型

yuyi_value = (W("吉祥") | W("喜庆") | W('如意')|W("富贵") | W("平安") | W('庄严')|W("庄重") | W("春节") | W('福寿') | W('简单')|W("美好") | W("高雅") | W('祥瑞')| W('神圣'))
chaodai_value = (W("宋朝") | W("宋代") | W('宋时期')| W("清朝") | W("清代") | W('唐朝')|W("唐代") | W("汉朝") | W('汉代')| W('元朝')|W("商朝")|W("明朝")|W("明代")|W("三国时期")| W("战国")| W("春秋")|W("新石器时代")| W("晋朝"))
caizhi_value = (W("漆器")|W("玉器")|W("玻璃器")|W("珐琅")|W("金银锡器")|W("陶瓷")|W("青铜器"))
yongtu_value = (W("乐器")|W("兵器")|W("水器")|W("度量衡")|W("烹饪器")|W("生活用具")|W("车马器")|W("酒器")|W("陈设器"))
gongyi_value = (W("彩绘")|W("剔红")|W("釉下彩")|W("雕塑")|W("镶嵌")|W("珐琅彩")|W("珍珠地")|W("颜色釉")|W("剔彩")|W("剔花"))
wenshi_value =  (W("鱼纹")|W("莲瓣纹")|W("水波纹")|W("弦纹")|W("龙纹")|W("菊花纹"))
category_value = (W("碗")|W("杯")|W("瓶")|W("壶")|W("盒")|W("盘"))
xingzhuang_value = (W("圆形")|W("长方形")|W("蒜头形")|W("扁形")|W("椭圆形")|W("柱状"))


yuyi_value_list = ["吉祥", "喜庆", "如意", "富贵", "平安", "庄严", "庄重", "春节", "福寿", "简单", "美好", "高雅", "祥瑞", "神圣"]
chaodai_value_list =  ["宋朝", "宋代", "宋时期", "清朝", "清代", "清朝时期", "唐朝", "唐代", "汉朝",  "汉代", "元朝","商朝","明朝","明代","三国时期","战国","春秋","新石器时代","晋朝"]
caizhi_value_list = ["漆器","玉器","玻璃器","珐琅","金银锡器","陶瓷","青铜器"]
yongtu_value_list = ["乐器","兵器","水器","度量衡","烹饪器","生活用具","车马器","酒器","陈设器"]
gongyi_value_list = ["彩绘","剔红","釉下彩","雕塑","镶嵌","珐琅彩","珍珠地","颜色釉","剔彩","剔花"]
wenshi_value_list = ["鱼纹","莲瓣纹","水波纹","弦纹","龙纹","菊花纹"]
category_value_list = ["碗","杯","瓶","壶","盒","盘"]

wenwu_info = (chaodai | category | wenshi | gongyi | yuyi | caizhi | xingzhuang | yongtu)
wenwu_value = (chaodai_value | category_value | wenshi_value | gongyi_value | yuyi_value | caizhi_value | xingzhuang_value | yongtu)
wenwu_count =  (W("多少")|W("计算")|W("几件"))
wenwu_lieju =  (W("哪些")|W("什么"))

"""
问题SPARQL模版
"""
class QuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_wenwu_info(word_objects):
        """
        某文物的属性
        :param word_objects:
        :return:
        """
        keyword = None

        for r in basic_wenwu_info:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None

        for value in word_objects:
            print(value.token, value.pos)

        for w in word_objects:
            if w.pos == pos_wenwu:
                e = u"?b :中文名 '{wenwu}'." \
                    u"?b {keyword} ?x.".format(wenwu=w.token, keyword=keyword)
                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)

                break

        return sparql

    @staticmethod
    def has_wenwu_chaodai(word_objects):
        """
        宋朝的文物有哪些
        :param word_objects:
        :return:
        """
        keyword = None
        value = None
        keyword_value = []
        for r in keyword_wenwu_info:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        print(keyword)
        if keyword == ":寓意":
            keyword_value = yuyi_value_list
        elif keyword == ":材质":
            keyword_value = caizhi_value_list
        elif keyword == ":用途":
            keyword_value = yongtu_value_list
        elif keyword == ":纹饰":
            keyword_value = wenshi_value_list
        elif keyword == ":工艺":
            keyword_value = gongyi_value_list
        elif keyword == ":朝代":
            keyword_value = gongyi_value_list
        for value in word_objects:
            print(value.token, value.pos)
        for w in word_objects:
            print(w.token)
            if w.token in keyword_value:
                print("okk")
                if keyword == ":朝代":
                    w = w[0]
                e = u"?b {keyword} '{value}'." \
                    u"?b :中文名 ?x.".format(value=w.token, keyword=keyword)
                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)
                break
        return sparql

    @staticmethod
    def has_wenwu_property(word_objects):
        """
        查询具有某属性的文物
        寓意为吉祥的文物有哪些
        材质为陶瓷的文物有哪些
        宋朝的文物有哪些
        :param word_objects:
        :return:
        """
        keyword = None
        value = None
        keyword_value = []
        for r in keyword_wenwu_info:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        print("keyword:",keyword)
        if keyword == ":寓意":
            keyword_value = yuyi_value_list
        elif keyword == ":材质":
            keyword_value = caizhi_value_list
        elif keyword == ":用途":
            keyword_value = yongtu_value_list
        elif keyword == ":纹饰":
            keyword_value = wenshi_value_list
        elif keyword == ":工艺":
            keyword_value = gongyi_value_list
        elif keyword == ":朝代":
            keyword_value =chaodai_value_list

        for w in word_objects:
            print(w.token)
            if w.token in keyword_value:
                print("okk")
                if keyword == ":朝代":
                    w = w.token[0]
                    print(w)
                    e = u"?b {keyword} '{value}'." \
                        u"?b :中文名 ?x.".format(value=w, keyword=keyword)
                else:
                    e = u"?b {keyword} '{value}'." \
                        u"?b :中文名 ?x.".format(value=w.token, keyword=keyword)
                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)
                break
        return sparql

    @staticmethod
    def has_wenwu_count(word_objects):
        """
        宋朝的文物有多少件
        :param word_objects:
        :return:
        """
        keyword = None
        value = None
        keyword_value = []
        for r in keyword_wenwu_info:
            keyword = r.apply(word_objects)
            if keyword is not None:
                break

        select = u"?x"
        sparql = None
        print("keyword",keyword)
        if keyword == ":寓意":
            keyword_value = yuyi_value_list
        elif keyword == ":材质":
            keyword_value = caizhi_value_list
        elif keyword == ":用途":
            keyword_value = yongtu_value_list
        elif keyword == ":纹饰":
            keyword_value = wenshi_value_list
        elif keyword == ":工艺":
            keyword_value = gongyi_value_list
        elif keyword == ":朝代":
            keyword_value =chaodai_value_list
        for w in word_objects:
            if w.token in keyword_value:
                if keyword == ":朝代":
                    w = w.token[0]
                    print(w)
                    e = u"?b {keyword} '{value}'." \
                        u"?b :中文名 ?x.".format(value=w, keyword=keyword)
                else:
                    e = u"?b {keyword} '{value}'." \
                        u"?b :中文名 ?x.".format(value=w.token, keyword=keyword)
                sparql = SPARQL_COUNT_TEM.format(prefix=SPARQL_PREFIX, select=select, expression=e)
                break
        return sparql



wenwu_info_rules = [
    Rule(condition_num=1, condition=wenwu_entity + Star(Any(), greedy=False) + wenwu_info + Star(Any(), greedy=False), action=QuestionSet.has_wenwu_info),
    Rule(condition_num=1, condition=(Star(Any(), greedy=False) + wenwu_info + Star(Any(), greedy=False) + wenwu_value +Star(Any(), greedy=False)  + wenwu_count+ Star(Any(), greedy=False))|(Star(Any(), greedy=False)  + wenwu_value +Star(Any(), greedy=False) + wenwu_count+ Star(Any(), greedy=False))  , action=QuestionSet.has_wenwu_count),
    Rule(condition_num=1, condition=(Star(Any(), greedy=False) + wenwu_info + Star(Any(), greedy=False) + wenwu_value + Star(Any(), greedy=False)+ wenwu_lieju +  Star(Any(), greedy=False) )|(Star(Any(), greedy=False) +  wenwu_value + Star(Any(), greedy=False)+ wenwu_lieju +  Star(Any(), greedy=False)), action=QuestionSet.has_wenwu_property),
 ]

# 对问句中出现的关键词进行匹配
basic_wenwu_info = [
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + chaodai + Star(Any(), greedy=False), action=WenwuPropertyValueSet.return_wenwu_info_chaodai_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + wenshi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_wenshi_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + gongyi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_gongyi_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + yuyi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yuyi_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + yongtu + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yongtu_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + caizhi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_caizhi_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + yaokou + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yaokou_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + category + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_category_value),
    KeywordRule(condition=wenwu_entity + Star(Any(), greedy=False) + xingzhuang + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_xingzhuang_value)
]

keyword_wenwu_info = [
    KeywordRule(condition=Star(Any(), greedy=False)+ chaodai_value  + Star(Any(), greedy=False) , action=WenwuPropertyValueSet.return_wenwu_info_chaodai_value),
    KeywordRule(condition= chaodai + Star(Any(), greedy=False), action=WenwuPropertyValueSet.return_wenwu_info_chaodai_value),
    KeywordRule(condition= Star(Any(), greedy=False) + wenshi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_wenshi_value),
    KeywordRule(condition= Star(Any(), greedy=False) + gongyi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_gongyi_value),
    KeywordRule(condition= Star(Any(), greedy=False) + yuyi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yuyi_value),
    KeywordRule(condition=Star(Any(), greedy=False) + yongtu + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yongtu_value),
    KeywordRule(condition= Star(Any(), greedy=False) + caizhi + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_caizhi_value),
    KeywordRule(condition= Star(Any(), greedy=False) + yaokou + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_yaokou_value),
    KeywordRule(condition=Star(Any(), greedy=False) + category + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_category_value),
    KeywordRule(condition= Star(Any(), greedy=False) + xingzhuang + Star(Any(), greedy=False),action=WenwuPropertyValueSet.return_wenwu_info_xingzhuang_value)
]