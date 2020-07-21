# -*- coding:utf-8 -*-

from inference.wenwu_info_template import wenwu_info_rules


class Query2Sparql:
    def __init__(self):
        self.wenwu_info_rules = wenwu_info_rules

    def parse(self, question_label):
        """
        解析问题模型
        :return:
        """
        sparql_list = []
        # 尝试wenwu信息解析
        for rule in self.wenwu_info_rules:
            sparql, num = rule.apply(question_label)
            if isinstance(sparql, list) and sparql:
                for temp_sparql in sparql:
                    sparql_list.append((num, temp_sparql))
                continue
            if sparql:
                sparql_list.append((num, sparql))
                continue

        return sparql_list
