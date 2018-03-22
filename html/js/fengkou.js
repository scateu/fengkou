var canvas, ctx, floatingWords = [];

var prefix_only = ["新旧动能转换下的", "存在性", "高通量", "普惠", "泛", "海绵型", "实时", "绿色", "海洋", "热", "冷", "湿", "可逆", "全天候", "全方位", "共享", "精准", "沉浸式", "透明", "扁平", "海量", "一带一路", "自主", "可控", "弹性", "平台型", "可信", "万物", "自动", "智慧", "未来", "数字", "无人", "硬", "高", "重", "轻", "轻量", "快", "慢", "快速", "高速", "强", "新", "软", "黑", "灰度", "多", "e", "i", "和谐", "确保", "深度", "行为", "动态", "静态", "可持续", "大规模", "全面", "现代", "理论" ];

var suffix_only = ["创新与发展", "交锋", "酒馆", "指纹", "感", "盾", "价值评估", "分布式", "预警", "边界", "边疆", "发展", "社区", "宝", "建模", "模型", "标准制订", "能力交付", "探秘", "产业联盟", "高峰论坛", "感知", "驱动", "+", "2.0", "大脑", "小镇", "名片", "正能量", "运营", "自信", "黑洞"];

var both = ["存在性风险", "空天地", "再生", "去中心化", "垂直化", "压缩", "效能", "拓扑", "随机", "梯度", "二级相变", "网格", "差分", "矩阵", "全息", "云", "拟态", "金融", "隐私", "保护", "一体化", "定制化", "规模化", "创新", "农业", "挖掘", "防御", "资源", "整合", "融合", "框架", "协同", "模拟", "执行", "赋力", "赋能", "沙盒", "沙盘", "勒索", "攻击", "体系", "能力", "平台", "3D", "文化", "表征", "量子计算", "驾驶", "汽车", "车联网", "物联网", "网联", "智能", "大数据", "可视化", "云计算", "Android", "情报", "系统", "人工智能", "机器学习", "跨平台", "安全水位", "单车", "能源", "充电", "漏洞", "威胁", "计算", "等保", "数据泄漏", "卷积神经网络", "民主设计", "传感网", "医疗", "无人机", "可穿戴", "机器人", "投顾", "出行", "识别", "人脸", "城市", "计算机视觉", "人机交互", "知识图谱", "生理传感", "芯片", "脑机接口", "创投", "深公司", "传媒", "科研", "区块链", ];

function FloatingWord(s) {
  this.pos = {
    x: Math.random() * canvas.width,
    y: Math.random() * 0.96 * canvas.height + canvas.height * 0.02
  },
  this.speed = Math.random() * 4 + 2,
  this.font =  Math.round(Math.random() * 10 + 14) + "px sans-serif",
  //this.font =  "24px sans-serif",
  this.text = s;
  ctx.font = this.font; // preloads font
  this.width = ctx.measureText(this.text).width;
}

FloatingWord.prototype.update = function() {
  this.pos.x += this.speed;
  if (this.pos.x >= canvas.width) {
    this.pos.x = -this.width;
    this.pos.y = Math.random() * 0.96 * canvas.height + canvas.height * 0.02;
  }
  ctx.font = this.font;
  ctx.fillText(this.text, this.pos.x, this.pos.y);
}


function animateWords() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgba(255,255,255,30)";
  for (var i = 0; i < floatingWords.length; i++) {
    floatingWords[i].update();
  }
  requestAnimationFrame(animateWords);
}

Array.prototype.randomElement = function () {
  return this[Math.floor(Math.random() * this.length)]
}

var s = suffix_only.concat(both);
var p = prefix_only.concat(both);

function createFloatingWords(n) {
   for (var i = 0; i < n; i++) {
     a = p.randomElement()
     b = s.randomElement()
     while (a == b) {
           b = s.randomElement();
     }
     floatingWords.push(
       new FloatingWord(a+b)
     );
   }
   console.log(floatingWords[0]);
   animateWords();
}

$(document).ready(function() {

  $(window).resize(function(event) {
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    canvas.width = $(window).width();
    canvas.height = $(window).height();
  }).trigger("resize");

  createFloatingWords(150);

})
