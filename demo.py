#!/usr/bin/env python
#-*- coding:utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import random

prefix_only = [ 
        "量子计算",
        "透明",
        "扁平",
        "海量",
        "一带一路",
        "自主",
        "可控",
        "弹性",
        "平台型",
        "可信",
        "万物",
        "自动",
]

suffix_only = [
        "驱动",
        "+", 
]

both = [
        "驾驶",
        "汽车",
        "车联网",
        "物联网",
        "网联",
        "智能",
        "大数据", 
        "可视化",
        "云计算",
        "Android",
        "情报",
        "感知",
        "系统",
        "人工智能",
        "机器学习",
        "跨平台",
        "安全水位",
        "漏洞",
        "威胁",
        "计算",
        "等保",
        "数据泄漏",
#        "不忘初心",
#        "方得始终",
        "价值评估",
#       "让世界变得更美好",
        "卷积神经网络",
        "民主设计",
        "传感网",
        ]

a = random.choice(prefix_only+both)
b = random.choice(suffix_only+both)

while a == b :
    a = random.choice(prefix_only+both)
    b = random.choice(suffix_only+both)
    

print("%s%s"%(a,b),end=' ')

