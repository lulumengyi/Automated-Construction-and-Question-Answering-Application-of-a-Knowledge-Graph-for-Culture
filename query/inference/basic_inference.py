# -*- coding:utf-8 -*-

"""
基于规则的推理
------------
公共模块
"""
from refo import finditer, Predicate
import re

class W(Predicate): # 关键词定义
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2


class Rule(object): # 问句匹配规则
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition_num = condition_num
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        matches = []
        # 文物 nz
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        return self.action(matches), self.condition_num

class KeywordRule(object):# 关键词匹配规则
    def __init__(self, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        if len(matches) == 0:
            return None
        else:
            return self.action()

"""
前缀和模版
"""
SPARQL_PREFIX = u"""PREFIX : <http://kg.BLCU.edu/ontology/property/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""
SPARQL_SELECT_TEM = u"{prefix}\n" + \
                    u"SELECT DISTINCT {select} WHERE {{\n" + \
                    u"{expression}\n" + \
                    u"}}\n " + \
                    u"LIMIT 10"

SPARQL_COUNT_TEM = u"{prefix}\n" + \
                   u"SELECT (COUNT(DISTINCT {select}) AS ?count) WHERE {{\n" + \
                   u"{expression}\n" + \
                   u"}}\n" + \
                   u"LIMIT 10"

SPARQL_ASK_TEM = u"{prefix}\n" + \
                 u"ASK {{\n" + \
                 u"{expression}\n" + \
                 u"}}\n"

"""
定义关键词
"""
pos_wenwu = "nz"
pos_other = "n"
pos_number = "m"

wenwu_entity = (W(pos=pos_wenwu))
other_entity = (W(pos=pos_other))
number_entity = (W(pos=pos_number))

class WenwuPropertyValueSet:
    def __init__(self):
        pass

    @staticmethod
    def return_wenwu_info_chaodai_value():
        return u":朝代"

    @staticmethod
    def return_wenwu_info_wenshi_value():
        return u":纹饰"

    @staticmethod
    def return_wenwu_info_category_value():
        return u":类型"

    @staticmethod
    def return_wenwu_info_gongyi_value():
        return u":工艺"

    @staticmethod
    def return_wenwu_info_yuyi_value():
        return u":寓意"

    @staticmethod
    def return_wenwu_info_yongtu_value():
        return u":用途"

    @staticmethod
    def return_wenwu_info_yaokou_value():
        return u":窑口"

    @staticmethod
    def return_wenwu_info_caizhi_value():
        return u":材质"

    @staticmethod
    def return_wenwu_info_xingzhuang_value():
        return u":形状"

    # @staticmethod
    # def return_book_person_introduction_value():
    #     return u":book_person_introduction"
