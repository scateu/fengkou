#!/usr/bin/env python
#-*- coding:utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import random

prefix_only = [ 
        "精准",
        "沉浸式",
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
        "智慧",
]

suffix_only = [
        "探秘",
        "高峰论坛",
        "感知",
        "驱动",
        "+", 
        "2.0",
]

both = [
        "量子计算",
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
        "医疗",
        "无人机",
        "可穿戴",
        "机器人",
        "投顾",
        "出行",
        "识别",
        "人脸",
        "城市",
        "计算机视觉",
        "人机交互",
        "知识图谱",
        "生理传感",
        "芯片",
        "脑机接口",
        "创投",
        "深公司",
        "传媒",
        "科研",
        "区块链",
        ]

def roll():
    _prefix = prefix_only+both
    _suffix = suffix_only+both
    a = random.choice(_prefix)
    b = random.choice(_suffix)
    
    while a == b :
        a = random.choice(_prefix)
        b = random.choice(_suffix)
    return a+b
    

#print("%s"%(a,b),end=' ')
#print("%s即将成为下一个风口。"%(roll()),end=' ')
print("随着%s的式微，以及%s的大潮落幕。%s即将成为下一个风口。"%(roll(),roll(),roll()))
