#!/usr/bin/env python
#-*- coding:utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import random

prefix_only = [ "热", "冷", "湿", "可逆", "全天候", "全方位", "共享", "精准", "沉浸式", "透明", "扁平", "海量", "一带一路", "自主", "可控", "弹性", "平台型", "可信", "万物", "自动", "智慧", "未来", "数字", "无人", "硬", "高", "重", "轻", "轻量", "快", "慢", "快速", "高速", "强", "新", "软", "黑", "灰度", "多", "e", "i", "和谐", "确保", "深度", "行为", "动态", "静态", "可持续", "大规模", "全面", "现代", "理论", ]

suffix_only = [ "价值评估", "分布式", "预警", "边界", "边疆", "发展", "社区", "宝", "建模", "模型", "标准制订", "能力交付", "探秘", "产业联盟", "高峰论坛", "感知", "驱动", "+", "2.0", "大脑", "小镇", "名片", "正能量", "运营", "自信", ]

both = [ "金融", "隐私", "保护", "一体化", "定制化", "规模化", "创新", "农业", "挖掘", "防御", "资源", "整合", "融合", "框架", "协同", "模拟", "执行", "赋力", "赋能", "沙盒", "沙盘", "勒索", "攻击", "体系", "能力", "平台", "3D", "文化", "表征", "量子计算", "驾驶", "汽车", "车联网", "物联网", "网联", "智能", "大数据", "可视化", "云计算", "Android", "情报", "系统", "人工智能", "机器学习", "跨平台", "安全水位", "单车", "能源", "充电", "漏洞", "威胁", "计算", "等保", "数据泄漏", "卷积神经网络", "民主设计", "传感网", "医疗", "无人机", "可穿戴", "机器人", "投顾", "出行", "识别", "人脸", "城市", "计算机视觉", "人机交互", "知识图谱", "生理传感", "芯片", "脑机接口", "创投", "深公司", "传媒", "科研", "区块链", ]

def roll():
    _prefix = prefix_only+both
    _suffix = suffix_only+both
    a = random.choice(_prefix)
    b = random.choice(_suffix)
    
    while a == b :
        a = random.choice(_prefix)
        b = random.choice(_suffix)
    return a+b
    
if __name__ == "__main__":
    print("%s"%(roll()))
    #print("%s即将成为下一个风口。"%(roll()),end=' ')
    #print("随着%s的式微，以及%s的大潮落幕。%s即将成为下一个风口。"%(roll(),roll(),roll()))
