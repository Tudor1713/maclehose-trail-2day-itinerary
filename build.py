# -*- coding: utf-8 -*-
"""生成单文件 HTML 日程表：麦理浩径第二段 · 万宜水库—破边洲—西湾露营"""
import os, base64, io
from PIL import Image

WS = r"C:\Users\Administrator\.minimax\sessions\mvs_885f562d9b9d4da7aae829386289e72e\workspace"
FIN = os.path.join(WS, "img", "final")
OUT = os.path.join(WS, "麦理浩径第二段_深圳往返徒步日程表.html")

def b64(name, maxw=1100, q=70):
    p = os.path.join(FIN, name + ".jpg")
    if not os.path.exists(p):
        return None
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if w > maxw:
        im = im.resize((maxw, round(h * maxw / w)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

PICNAMES = ["popin", "popin2", "conic", "eastdam", "eastdam2", "reservoir", "reservoir2",
            "rhyolite", "highisland", "saiwan", "hamtin", "tailong", "tailong2", "tailong3",
            "szx_t3", "szx_t3b", "szx_gate"]

# 每张图只生成一次, 以 CSS 类复用, 避免同一张图重复内嵌
PICCSS = []
for n in PICNAMES:
    d = b64(n, 1500 if n == "popin" else 1100, 74 if n == "popin" else 70)
    if d:
        PICCSS.append(f".pic-{n}{{background-image:url({d})}}")

def img(name, cls="", alt=""):
    """返回使用背景图的 div, 图片本体只在 CSS 中存储一份"""
    if f"pic-{name}" not in "".join(PICCSS):
        return ""
    return (f'<div class="pic {cls} pic-{name}" role="img" aria-label="{alt}"></div>')

# ---------------------------------------------------------------- 数据
D2 = [
    ("06:30", "深圳出发", "住处的酒店 → 福田口岸", "地铁4/10号线或打车,约25分钟;4人行李多建议打车", "退房时把不带上山的行李寄存", "cost"),
    ("07:35", "过关完成", "落马洲站 → 叫的士", "工作日早晨人流远小于周末,过关顺利;出站左转跟「公共运输交汇处」指示牌", "叫车请指名要「绿色新界的士」", "transit"),
    ("08:40", "抵达东坝", "万宜水库东坝 M018", "破边洲段入口,亦是联合国地质公园核心区;打车到坝尾即到", "四车同行更划算", "photo"),
    ("09:00", "东坝六角岩柱", "1.4亿年前超级火山遗迹", "柱状节理流纹岩,海蚀崩塌形成的六边形石柱群,是香港地质公园的封面;工作日几乎没人,可从容拍照", "停留20分钟", "photo"),
    ("09:20", "破边洲支线", "往返约2.8km · 上下山1.5-2小时", "从东坝右侧上山,翻越山坳俯瞰整片六角岩柱海岸,崖边有围栏,切勿跨越", "全程暴晒", "photo"),
    ("11:00", "东坝 → 浪茄湾", "石板栈道 1.5km", "顺麦理浩径下行,20分钟翻过山头再下到沙滩,这里是一二段的分界点 M020", "下坡好走", "photo"),
    ("12:00", "浪茄湾", "白沙 + 果冻海", "细软白沙与澄澈海水;此段无补给无淡水,午餐需自带", "停留40分钟", "photo"),
    ("12:40", "浪茄湾 → 西湾山", "爬升约300m · 全程无遮荫", "本段最辛苦:山体从海平面突兀而起,路窄坡陡,登山杖必备,10月底体感仍可达38°C", "约1.5小时", "photo"),
    ("14:35", "下坡 → 吹筒坳 → 西湾村", "水泥路下坡", "途中经过西湾观星台与日出方位仪,是露营党最爱的打卡点", "约1小时", "photo"),
    ("15:25", "西湾村补给", "士多店 · 公厕 · 淡水", "全线最后一个像样的补给点,买水买干粮;另有山水豆腐花、公仔面", "停留50分钟", "photo"),
    ("16:15", "抵达西湾营地", "大浪西湾北面沙滩", "注意:营地在北面沙滩,士多那边的南面沙滩不是营地;有标准厕所与水喉", "扎营50分钟", "photo"),
    ("17:25", "黄昏时段", "沙滩 / 观星台 / 日落", "工作日露营客极少,整片沙滩基本只有你们四人;退潮时海水呈现荧光蓝", "自由活动", "free"),
    ("19:25", "晚餐 + 星空", "西湾观星台 270°", "没有光污染的海岸,肉眼可见银河;10月底夜里海边风大,备防风外套", "注意野猪", "free"),
]

SPOTS = [
    ("东坝 / 万宜水库", "M018", "reservoir", "eastdam",
     "麦理浩径第二段的起点,也是香港联合国世界地质公园的核心。1.4亿年前的超级火山喷发,熔岩冷却时形成六边形柱状节理,后来被海浪掏空崩塌,造就了这片像乐高一样规整又奇异的石柱群。水库本身是香港重要的食水设施,坝尾有凉亭与旱厕,但不卖饮用水。",
     [("徒步里程", "起点 M018"), ("停留", "25-30 分钟"), ("看点", "六角岩柱群"), ("补给", "无·仅凉亭旱厕")]),
    ("破边洲", "支线 2.8km", "conic", "popin2",
     "东坝旁边那座独立小岛,原是半岛山体,因海蚀洞不断坍塌才与陆地分离。岛上同样布满六角岩柱,配上深蓝海水,随手一拍就是《国家地理》封面。观景台在半山腰,是无遮挡的绝佳机位;脚下悬崖有围栏,请勿翻越。",
     [("往返里程", "约 2.8 km"), ("耗时", "1.5-2 小时"), ("强度", "上下山各约20分钟"), ("提示", "全程无遮荫,极晒")]),
    ("浪茄湾", "M020", "tailong2", "rhyolite",
     "一二段的分界点,一段与二段在此交接。细白沙配渐变蓝绿的海水,晴天时美得像手机壁纸,也是很多人在此露营的经典选择。缺点是:没有商店、没有淡水,水要提前备足。沙滩背后是戒毒所,有淡水但不对外开放。",
     [("距离", "东坝 1.5 km"), ("徒步", "约 1 小时"), ("沙质", "细白沙"), ("补给", "无·必须自带")]),
    ("西湾山", "海拔 314m", "highisland", "rhyolite",
     "全程最累的一段,山体从海平面突兀拔起,海拔虽只有 314 米,爬起来却像爬了六百米。几乎全程无树荫、无遮蔽,上到山脊后山风会瞬间变得凉爽。下山途中会经过西湾观星台和日出方位仪,晚上可以摸黑上来数星星。",
     [("爬升", "约 300 m"), ("耗时", "1.5-1.75 小时"), ("难度", "★★★☆☆ 全程暴晒"), ("建议", "登山杖必带")]),
    ("西湾", "M082 附近", "saiwan", "tailong3",
     "大浪四湾(东湾、大湾、咸田湾、西湾)里最大的一个,一片大礁石把沙滩一分为二。官方指定的大型营地,位在<b>大浪西湾北面沙滩</b>(注意:南面近士多的那片沙滩并非营地),沿岸有标准厕所与水喉,但冲凉要另外付费。西湾村有多家士多,能买到山水豆腐花和公仔面;附近还有观星台与日出方位仪,是全香港数一数二的观星位置。工作日露营客极少,整片沙滩基本只有你们四人。",
     [("位置", "M082 标距柱附近"), ("沙质", "细·水清"), ("配套", "旱厕·水喉·士多"), ("洗澡", "约30-40港币/人")]),
    ("咸田湾", "顺路可选", "hamtin", "tailong",
     "就在西湾旁边的第四片沙,有一座著名的独木桥和海风士多。沙滩前段最开阔,常能看到远方的蚺蛇尖。如果 D3 早上还有时间,可以从这里拍日出,或者走一段海岸线看四湾相连的全景。",
     [("位置", "M089-M090 之间"), ("特色", "独木桥·开阔沙滩"), ("配套", "海风士多·快艇"), ("距西湾", "约 2 km")]),
]

TRANSIT_GO = [
    ("A", "拼的士直达东坝", "推荐", "10/28 早上:福田口岸过关 → 落马洲站叫绿色新界的士 → 东坝", "约 55 分钟", "350-390 港币 / 车 · 人均 88-98", "四人分摊最划算;务必指名绿色新界的士,红色贵一半"),
    ("B", "港铁 + 巴士 + 打的士", "最省钱", "落马洲 → 沙田(东铁线) → 西贡(299X) → 西贡总站叫的士 → 东坝", "约 2 小时 40 分", "约 220 港币 / 人", "10/28 是工作日,9A 小巴不开,必须在西贡改打车"),
    ("C", "跨境包车", "最省心", "深圳指定点 → 直达东坝,不过境", "约 70-90 分钟", "约 400-600 港币 / 车 · 人均 100-150", "需提前预约;四人平摊与方案A相近"),
]

TRANSIT_BACK = [
    ("R1", "拼车 + 城巴 B3X + 地铁/打车", "推荐,最平衡", "西湾村 →(步行/的士)→ 西湾亭 →(拼的士经清水湾隧道)→ 屯门 →(城巴 B3X)→ 深圳湾口岸 →(地铁4号线或打车)→ 深圳北站", "约 2 小时 20 分", "人均约 190 港币", "对应 14:32 的 G2930 高铁;B3X 每日 06:15-23:05,08:05 后每 10 分钟一班,全程 16.5 港币"),
    ("R2", "全公共交通", "最省钱", "西湾村 →(NR29 村巴)→ 西贡 →(299X)→ 沙田 →(东铁线)→ 落马洲 → 福田口岸 → 地铁4号线 → 深圳北站", "约 4 小时 15 分", "约 120 港币 / 人", "村巴每天日间服务,工作日班次较少,务必当天再查一次"),
    ("R3", "拼车 + B3X → 宝安机场 T3", "若改坐 17:00 航班", "西湾村 →(拼的士)→ 屯门 →(城巴 B3X)→ 深圳湾口岸 → 蛇口 → 宝安机场 T3", "约 2 小时 20 分", "人均约 190 港币", "08:45 到机场,余量 8 小时;代价是 06:25 就得拔营,放弃日出"),
    ("R4", "跨境包车直达机场", "最省心,适合行李多", "西湾 → 宝安机场 T3,一车到底走皇岗/文锦渡", "约 2.5 小时", "约 800-1500 港币 / 车 · 人均 200-375", "四人平摊仍高于 R1,但最不赶;需提前 4 小时预约"),
]

GEAR = [
    ("必须带", "core", [
        ("港澳通行证 + 有效签注", "深圳居民办「一签多行」或「一年多次」,过关用"),
        ("八达通 + 少量港币现金", "小巴只收八达通或现金,士多用现金;备 500 港币零钱"),
        ("2 升以上饮用水", "浪茄湾到西湾全程无补给,山上一点水都买不到"),
        ("防滑徒步鞋 + 登山杖", "破边洲礁石极滑,西湾山陡坡多,杖能省一半腿力"),
        ("SPF50 防晒 + 帽 + 冰袖", "10 月香港紫外线仍 6-11 级,全程无树荫"),
        ("头灯 + 备用电池", "营地与山径无照明,夜间观星必备"),
        ("雨衣", "山径多为无遮挡,雷雨说来就来"),
        ("垃圾袋", "西湾没有垃圾桶,执法已查获 26 宗乱丢垃圾个案"),
    ]),
    ("露营相关", "camp", [
        ("帐篷 + 地钉(用长钉)", "沙地地钉易松,建议长地钉或压重"),
        ("睡袋(舒适温标 10°C)", "秋冬夜间海边可降至 10°C 以下,风大体感更低"),
        ("防潮垫", "沙地隔湿隔潮,否则整夜睡在潮地上"),
        ("卡式炉 + 气罐", "营地禁止明火,只能用自带气罐炉具"),
        ("食物密封袋 + 挂绳", "野猪会攻击帐篷和食物,必须离地高挂"),
        ("头灯 + 充电宝", "营地无插座,充电宝是唯一电源"),
    ]),
    ("实用可选", "nice", [
        ("驱蚊水 / 蚊怕", "沙滩草丛蚊虫多,晚上尤其厉害"),
        ("急救包 + 云南白药", "野外磕碰擦伤常备"),
        ("离线地图(两步路/户外助手)", "山里部分路段无信号,M 标距柱可定位"),
        ("快干衣 + 换洗衣物", "备用一套,湿衣可晾干"),
        ("折叠小凳", "营地可用,比坐石头舒服"),
    ]),
]

WARN = [
    ("10/29 是工作日,破边洲不需要预约", "good",
     "这是你们最大的运气。渔护署的「万宜地质步道—破边洲段」预约制只覆盖 2026 年 9 月 5 日至 10 月 7 日期间的周末、中秋节与国庆黄金周,适用日期为 9/5-6、9/12-13、9/19-20、9/25-27 与 10/1-7。10 月 29 日是星期四,不在指定日期内,进入破边洲段无须预约,直接去即可。工作日东坝人流也远低于周末,六角岩柱可以拍到没有其他人的画面。"),
    ("工作日 9A 小巴不开,必须打车", "critical",
     "从北潭涌到东坝的 9A 专线小巴仅在周末及公众假期运行,10/29 是星期四,不开。若坚持坐公共交通,须在沙田/大学乘东铁线到西贡(299X),再从西贡总站叫的士到东坝,车费约 160 港币/车。四人分摊比直接拼车更贵,建议直接约车。"),
    ("西湾营地在北面沙滩,不是士多那边", "high",
     "渔护署官方营地页面写明:西湾营地位于大浪西湾「北面沙滩」,沿麦理浩径第二段路旁;「西湾南面的沙滩(近士多)并非露营地点」。营内有标准厕所与水喉(水喉),但洗澡需另外付费,约 30-40 港币/人,须自带洗漱用品与拖鞋。从西湾村走到营地还有约 5 分钟步程。"),
    ("工作日士多可能提早关门,自带干粮", "high",
     "西湾村有多间士多经营,是全线最后一个补给点,但部分小店平日营业时间较弹性,关门可能早于周末,且只收港币现金、物价偏高(水 15-40 港币、泡面约 50 港币)。强烈建议 10/28 在深圳就把两天全部干粮与水备齐,不要指望现场买。"),
    ("夜间野猪出没", "high",
     "西湾一带野猪成群,会啃食食物、翻找垃圾袋。食物必须密封并高挂树上,不要留在帐篷内;也不要留下任何食物残渣——残渣既招野猪,又会被渔护署执法。"),
    ("潮水上涨,别把帐篷扎太靠海", "mid",
     "渔护署明确提示:西湾营地位于沙滩海岸边,露营人士必须特别小心潮水上涨。扎营时尽量往岸上挪,不要贴着水线;西湾营地有烧烤炉与标准厕所可使用。"),
    ("气罐不能过地铁安检", "mid",
     "地铁与多数口岸禁止携带气罐。建议在国内买好炉具,过关后于西贡士多或百货补充气罐;营地只允许自带气罐炉具,严禁明火。"),
    ("深圳机场截载时间", "mid",
     "若最终改订 17:00 航班:国内航班停止办理乘机手续为起飞前 38 分钟(南航 30 分钟,深航/国航/山航/昆明航空 35 分钟),登机口关闭为起飞前 20 分钟。官方建议国内航班至少提前 2-3 小时到达机场。"
     "若坐 14:32 的 G2930 高铁:深圳北站客流高峰在 6:00-10:00,建议提前 40 分钟以上到站,开车前 3 分钟停止检票。"),
]

FACTS = [
    ("10/28", "徒步露营 · 周三"),
    ("10/29", "返回深圳 · 周四"),
    ("2 天 1 夜", "紧凑行程"),
    ("4 人", "同行团队"),
    ("8.5-9 km", "徒步总里程"),
    ("约 300 m", "累计爬升(西湾山)"),
    ("5-6 h", "净徒步时间"),
    ("约 190 港币", "人均市内交通"),
]

# ---------------------------------------------------------------- HTML
def build():
    P = []
    A = P.append

    A('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">')
    A('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">')
    A('<title>麦理浩径第二段 · 万宜水库—破边洲—西湾露营 | 深圳往返徒步日程表</title>')
    A('<meta name="description" content="深圳出发、两天一夜的麦理浩径第二段徒步日程表:万宜水库东坝、破边洲、浪茄湾、西湾山、西湾露营,含完整交通方案、耗时计算与返程赶机时间链。">')
    CSS = open(os.path.join(WS, 'light.css'), encoding='utf-8').read()
    A('<style>' + CSS + '''
</style>
<style>''' + "\n".join(PICCSS) + '''
</style></head>
<body>''')

    # NAV
    A('<nav><div class="nav-in">')
    A('<div class="logo"><i></i>MACLEHOSE · 02</div>')
    A('<div class="nav-links">')
    for h, t in [("#d1", "D1 徒步"), ("#d2", "D2 返程"),
                 ("#ticket", "往返车票"), ("#spots", "景点详解"), ("#transit", "市内交通"),
                 ("#gear", "装备清单"), ("#warn", "注意事项")]:
        A(f'<a href="{h}">{t}</a>')
    A('</div></div></nav>')

    # HERO
    A('<header><div class="hero-bg">' + img("popin", "heroimg", "破边洲六角火山岩柱与海岸") + '</div>')
    A('<div class="hero-in">')
    A('<div class="kicker">2026.10.28 — 10.29 · 两天一夜 · 4 人 · 深圳出发</div>')
    A('<h1>麦理浩径第二段<br><em>破边洲 · 万宜水库 · 西湾露营</em></h1>')
    A('<p class="hero-sub">第一天早上从深圳出发,过关进山,走完东坝六角岩柱、破边洲、浪茄湾与西湾山,'
      '当晚扎营西湾;第二天清晨看日出、从容撤回深圳,<b>14:32 乘 G2930 高铁回贵阳</b>。'
      '每一段车程、每一步徒步、每一个班次都已换算成钟点——'
      '<b>而且全程落在工作日,破边洲不需要预约</b>。</p>')
    A('<div class="pills">')
    A('<span class="pill">徒步 <b>8.5-9 km</b></span>')
    A('<span class="pill">累计爬升 <b>300 m</b></span>')
    A('<span class="pill">西湾露营 <b>1 晚</b></span>')
    A('<span class="pill">D1 起步 <b>09:00</b></span>')
    A('<span class="pill">D2 发车 <b>14:32</b></span>')
    A('<span class="pill">人均交通 <b>约 190 港币</b></span>')
    A('<span class="pill">破边洲 <b>免预约</b></span>')
    A('</div></div>')
    A('<div class="scroll-hint"><i></i>SCROLL</div></header>')

    # 关键数字
    A('<section id="d1"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">00 / AT A GLANCE</div>'
      '<h2>三天两夜,一张表看完</h2>'
      '<p class="sec-desc">把整趟行程压缩成六个关键数字,每一项都对应下文的详细拆解。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="facts reveal">')
    for v, l in FACTS:
        A(f'<div class="fact"><b>{v}</b><span>{l}</span></div>')
    A('</div></div></section>')

    # D1
    A('<section><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">NIGHT BEFORE / 前一晚</div>'
      '<h2>前一晚 · 在深圳准备就绪</h2>'
      '<p class="sec-desc">紧凑的两日行程,所有准备都要压在 10/27 晚上完成:'
      '<b>买齐两天干粮、办妥八达通和港币、确认签注有效</b>。'
      '第二天早上 06:30 就要出发过关,睡不够是这趟行程最大的风险。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="two-col">')
    A('<div class="card reveal">')
    A('<h3 style="margin:0 0 14px;font-size:18px">抵达当晚 · 5 件事</h3>')
    A('<div class="gear-list">')
    for t, s in [
        ("确认港澳通行证签注有效", "签注次数与有效期必须覆盖全程;深圳居民办「一签多行」最省心"),
        ("办好八达通并换现金", "小巴只收八达通或现金且不找零;建议备 500 港币小额"),
        ("买齐两天全部干粮", "工作日西湾士多关门早、只收现金、物价翻倍,深圳买齐最保险"),
        ("检查登山鞋与登山杖", "破边洲礁石极滑,杖不是可选项而是必需品"),
        ("加满 2 升以上饮用水", "浪茄湾到西湾全程无补给,山上水价翻几倍且不一定有得卖"),
        ("确认四人分摊方案", "去程拼的士 350-390 港币/车,人均约 88-98;约好在哪一站碰头"),
    ]:
        A(f'<div class="gear-item"><i></i><div><b>{t}</b><small>{s}</small></div></div>')
    A('</div></div>')
    A('<div class="card mini reveal">')
    A('<h4>住宿选址建议</h4>')
    A('<p>坐 <b>G2921 高铁</b>(10/27 11:14 发车)到深圳北站后,乘地铁 4 号线约 25 分钟直达福田口岸。'
      '住<b>福田口岸或会展中心一带</b>最省事:第一天早上 06:30 出门就能过关,'
      'D3 从福田口岸进深圳也顺路。</p>')
    A('<p>若改乘早班机 3U1314(09:40 到宝安),落地后打车到福田口岸约 40 分钟,'
      '时间依然够,但要多付机场到市区的一段车费。</p>')
    A('<h4 style="margin-top:20px">装备采购点</h4>')
    A('<p>深圳本地装备价格比香港低很多,<b>气罐除外</b>——气罐无法通过地铁与多数口岸安检。'
      '建议在国内买好炉具,到港后于西贡士多或百货补充气罐。</p>')
    A('</div>')
    A('</div></div></section>')

    # D1 徒步日 时间轴
    A('<section id="d1"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">DAY 1 / 10月28日 周三 · 徒步日</div>'
      '<h2>第一天 · 早上从深圳出发,走到西湾扎营</h2>'
      '<p class="sec-desc">06:30 从深圳住处出发,07:35 过关,09:00 从东坝起步。'
      '全天只有一件事:走完这段山海。'
      '<b>10/28 是工作日,9A 小巴不开,去程必须拼的士</b>——四人分摊,人均约 88 港币。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="tl">')
    for t, title, en, desc, note, kind in D2:
        A('<div class="tl-item reveal"><div class="tl-time">'+t+'</div><div class="tl-dot"></div>')
        A('<div class="tl-card">')
        if kind == "photo":
            A('<div class="tl-body">')
        else:
            A('<div class="tl-body">')
        # 图片分配
        photo_map = {
            "东坝六角岩柱": "eastdam2", "破边洲支线": "popin2",
            "东坝 → 浪茄湾": "rhyolite", "浪茄湾": "tailong2",
            "浪茄湾 → 西湾山": "highisland", "下坡 → 吹筒坳 → 西湾村": "reservoir2",
            "西湾村补给": "tailong3", "抵达西湾营地": "saiwan",
        }
        if kind == "photo" and title in photo_map:
            A('<div class="tl-h"><h3>'+title+'</h3><span class="tl-tag">'+en+'</span></div>')
            A('<p class="tl-p">'+desc+'</p>')
            A('<div class="tl-note">'+note+'</div>')
            A('<div class="tl-media">'+img(photo_map[title], "", title)+
              '<figcaption>'+desc+'</figcaption></div>')
        else:
            tagc = "tl-tag warm" if kind in ("cost", "transit") else "tl-tag"
            A('<div class="tl-h"><h3>'+title+'</h3><span class="'+tagc+'">'+en+'</span></div>')
            A('<p class="tl-p">'+desc+'</p>')
            A('<div class="tl-note">'+note+'</div>')
        A('</div></div></div>')
    A('</div>')

    A('<div class="card reveal" style="margin-top:28px">')
    A('<h3 style="margin:0 0 14px;font-size:18px">两套时间基准,出发前对号入座</h3>')
    A('<div class="tbl-wrap"><table><thead><tr>'
      '<th>方案</th><th>抵达东坝</th><th>开始徒步</th><th>扎营完成</th><th>营位与黄昏</th></tr></thead><tbody>')
    for nm, st, st2, camp2, note in [
        ("A 拼的士直达(推荐)", "08:40", "09:00", "16:15",
         "完整保留黄昏沙滩、观星台与整段星空时间"),
        ("B 港铁+巴士+的士", "10:55", "11:15", "18:30",
         "黄昏被压缩,建议放弃观星台,直接在西湾沙滩过夜"),
    ]:
        A(f'<tr><td class="t-name">{nm}</td><td class="t-time">{st}</td><td class="t-time">{st2}</td>'
          f'<td class="t-time">{camp2}</td><td class="t-route">{note}</td></tr>')
    A('</tbody></table></div>')
    A('<p style="margin:14px 0 0;font-size:13px;color:var(--mute)">'
      '注:9A 专线小巴(北潭涌—万宜水库东坝)<b style="color:var(--sun)">仅在周末及公众假期运行</b>,'
      '10/29 是星期四,不开。方案 B 需在西贡总站改乘的士,车费约 160 港币/车;'
      '四人分摊后人均约 220 港币,比方案 A 贵约 130 港币/人,还白白损失一个半小时的黄昏。'
      '<b style="color:var(--paper)">强烈建议直接拼的士。</b></p>')
    A('</div></div></section>')

    # D3
    A('<section id="d2"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">DAY 2 / 10月29日 周四 · 返程</div>'
      '<h2>第二天 · 从西湾撤回深圳,高铁返贵阳</h2>'
      '<p class="sec-desc">推荐搭 <b>14:32 的 G2930 高铁</b>:可以从容看完西湾日出、'
      '慢悠悠吃个早餐、逛完西湾村再走,'
      '<b>10:00 前离开营地即可</b>,完全不赶。这条链路的余量非常厚——即使塞车也不会误车。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="count reveal">')
    for v, l in [("07:00", "看日出"), ("08:00", "早餐拆营"), ("10:00", "离开西湾"),
                  ("12:45", "到深圳北站"), ("14:32", "G2930 发车")]:
        A(f'<div><b>{v}</b><span>{l}</span></div>')
    A('</div>')
    A('<div class="card reveal" style="margin-bottom:16px">')
    A('<h3 style="margin:0 0 12px;font-size:18px">D2 时间线 · 从西湾营地撤回深圳</h3>')
    A('<div class="tl" style="padding-left:0">')
    for t, title, desc in [
        ("07:00", "看西湾日出", "东面朝海,帐篷朝东开就能迎接第一缕光;这是整趟行程最值的 20 分钟"),
        ("08:00", "早餐 · 拆营", "收拾帐篷、带走全部垃圾;西湾没有垃圾桶,执法严查"),
        ("09:00", "西湾村补给与闲逛", "买手信、吃碗山水豆腐花;顺便在茶座看海,工作日几乎没人"),
        ("10:00", "离开西湾 → 西湾亭", "步行 2.5km 约 35 分钟;村口有 NR29 村巴与的士可搭"),
        ("10:40", "西湾亭 → 屯门", "拼的士经清水湾隧道约 40 分钟,约 300 港币/车,人均 75 港币"),
        ("11:15", "城巴 B3X → 深圳湾口岸", "屯门市中心上车,全程 16.5 港币,约 25 分钟;08:05 后每 10 分钟一班"),
        ("11:45", "深圳湾口岸过关", "一地两检,同楼完成两地手续,不用下车"),
        ("12:45", "深圳北站 · 候车", "蛇口打车约 25-30 分钟到深圳北;留 40 分钟安检,开车前 3 分钟停止检票"),
        ("14:32", "G2930 发车", "深圳北 → 虎门 → 广州南 → 佛山西 → 贺州 → 贵阳东"),
        ("19:40", "抵达贵阳东", "出站后打车或地铁转回家,行程结束"),
    ]:
        A(f'<div class="tl-item reveal"><div class="tl-time">{t}</div><div class="tl-dot"></div>'
          f'<div class="tl-card"><div class="tl-body"><div class="tl-h"><h3>{title}</h3></div>'
          f'<p class="tl-p">{desc}</p></div></div></div>')
    A('</div></div>')
    A('<div class="two-col">')
    A('<div class="card mini reveal" style="padding:0;overflow:hidden">')
    A('<div style="position:relative">')
    A(img("szx_t3", "", "深圳宝安机场 T3 航站楼出发层"))
    A('<div style="position:absolute;inset:auto 0 0 0;padding:34px 20px 14px;'
      'background:linear-gradient(transparent,rgba(8,16,20,.9));font-size:12px;color:#cfe0e3;z-index:2">'
      '深圳宝安机场 T3 航站楼出发层 · 国内值机岛 A-C / F-H</div>')
    A('</div>')
    A('<div style="padding:20px 22px">')
    A('<h4>备选:若最终订了 17:00 航班</h4>')
    A('<p><b>截载时间:</b>国内航班停止办理乘机手续为起飞前 <b>38 分钟</b>(南航 30 分钟,'
      '深航/国航/山航/昆明航空 35 分钟),登机口关闭为起飞前 20 分钟。</p>')
    A('<p><b>建议到达:</b>国内航班至少提前 <b>2-3 小时</b>;深圳机场高峰期建议提前 1.5-2 小时。'
      '本表目标定在 <b>14:30</b>。</p>')
    A('<p><b>值机岛:</b>国内航班值机岛为 A-C、F-H 岛,四层出发大厅。'
      'T3 登机口 301-378 在主航站楼,<b>501-583 在卫星厅</b>,过完安检后需乘捷运列车前往。</p>')
    A('<p><b>离港平台提醒:</b>T3 离港平台正处于交通综合提升改造期间,'
      '1-4 号门可能分阶段临时封闭,留客车道有占道施工,建议按现场指引预留更宽裕时间。</p>')
    A('<p><b>时间账:</b>若走航班方案,06:25 起床拆营 → 08:45 到 T3,'
      '等于<b>放弃西湾日出</b>——这是航班方案唯一真正的代价,其余时间都很宽裕。</p>')
    A('</div></div>')
    A('<div class="card mini reveal">')
    A('<div style="border-radius:11px;overflow:hidden;margin-bottom:16px">')
    A(img("szx_gate", "", "深圳宝安机场 T3 登机口"))
    A('</div>')
    A('<h4>深圳端接驳</h4>')
    A('<p><b>地铁 11 号线机场站</b>可直达 T3 航站楼,是最省心的方式,末班车约 23:30。</p>')
    A('<p><b>福田口岸 → T3</b>:地铁 11 号线约 35 分钟,或打车约 30-40 分钟(机场周边常堵)。</p>')
    A('<p><b>深圳湾口岸(蛇口)→ T3</b>:沿后海滨路往宝安方向,打车约 30-35 分钟最直接。</p>')
    A('<p><b>托运提醒:</b>露营装备体积大,建议用托运;充电宝、锂电池必须随身,不可托运。</p>')
    A('</div>')
    A('</div></div></section>')

    # 票务
    A('<section id="ticket"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">05 / BIG TRANSPORT</div>'
      '<h2>往返大交通 · 贵阳 ⇄ 深圳</h2>'
      '<p class="sec-desc">这趟行程的特殊之处在于:10/28 是工作日清晨出发,10/29 上午撤营、下午返程。'
      '下面把高铁与飞机的真实班次、票价和「时间够不够」逐条算给你看。</p></div>'
      '<div class="rule"></div></div>')

    GO = [
        ("G2921", "", "贵阳北 11:14", "深圳北 15:47", "4h33", "496.5", "15:47 到深,当晚从容安顿采购", True),
        ("G907", "", "贵阳北 11:49", "深圳北 16:31", "4h42", "497.5", "抵达 16:31,安顿时间略紧", False),
        ("G3735", "", "贵阳北 13:46", "深圳北 18:17", "4h31", "494.5", "抵达 18:17,采购时间偏少", False),
        ("G2945", "", "贵阳北 15:09", "深圳北 19:43", "4h34", "516.5", "偏晚,超市已关门", False),
        ("G2925", "", "贵阳北 18:53", "深圳北 23:25", "4h32", "493.5", "深夜抵深,当晚无法采购", False),
        ("3U1314", "fly", "贵阳 07:50", "深圳 09:40", "1h50", "680-1000", "早班机,白天可用时间最多", False),
        ("ZH9896", "fly", "贵阳 10:20", "深圳 11:50", "1h30", "680-1000", "飞行最快,午间抵深", False),
        ("CZ3667", "fly", "贵阳 16:15", "深圳 18:10", "1h55", "680-1000", "傍晚机,抵达即晚", False),
    ]
    A('<div class="grid g2">')
    A('<div class="ticket reveal">')
    A('<div class="ticket-h"><div class="tdate">10月27日 · 周二 · 去程</div>'
      '<h3>贵阳 → 深圳</h3><p>当天抵深住一晚,次日清晨过关进山</p></div>')
    A('<div class="ticket-body">')
    for code, cls, dep, arr, dur, price, note, pick in GO:
        A(f'<div class="tr{" pick" if pick else ""}">')
        A(f'<div class="tr-code {cls}">{code}{"<span class=\'tr-flag\'>推荐</span>" if pick else ""}</div>')
        A(f'<div class="tr-mid"><div class="tr-time">{dep}<small>→</small>{arr}'
          f'<small> · {dur}</small></div><div class="tr-note">{note}</div></div>')
        A(f'<div class="tr-price"><b>{"¥"+price if cls!="fly" else price}</b>'
          f'<small>{"二等座" if cls!="fly" else "经济舱"}</small></div>')
        A('</div>')
    A('</div></div>')

    BK = [
        ("G2966", "", "深圳北 08:08", "贵阳北 12:50", "4h41", "472.5", "需 05:40 起床,等于放弃日出", False),
        ("G2946", "", "深圳北 09:56", "贵阳北 14:40", "4h44", "494.5", "需 06:30 离西湾,很赶", False),
        ("G2930", "", "深圳北 14:32", "贵阳东 19:40", "5h08", "444.5", "从容撤退,能看完日出再走", True),
        ("G2922", "", "深圳北 16:08", "贵阳北 20:32", "4h24", "496.5", "时间最宽松,到贵阳天已黑", False),
        ("17:00 航班", "fly", "宝安T3 17:00", "贵阳约 19:35", "1h50", "680-1200", "需 06:25 拔营,放弃日出", False),
    ]
    A('<div class="ticket reveal">')
    A('<div class="ticket-h"><div class="tdate">10月29日 · 周四 · 返程</div>'
      '<h3>深圳 → 贵阳</h3><p>从西湾营地撤回深圳,赶车或赶机</p></div>')
    A('<div class="ticket-body">')
    for code, cls, dep, arr, dur, price, note, pick in BK:
        A(f'<div class="tr{" pick" if pick else ""}">')
        A(f'<div class="tr-code {cls}">{code}{"<span class=\'tr-flag\'>推荐</span>" if pick else ""}</div>')
        A(f'<div class="tr-mid"><div class="tr-time">{dep}<small>→</small>{arr}'
          f'<small> · {dur}</small></div><div class="tr-note">{note}</div></div>')
        A(f'<div class="tr-price"><b>{"¥"+price if cls!="fly" else price}</b>'
          f'<small>{"二等座" if cls!="fly" else "经济舱"}</small></div>')
        A('</div>')
    A('</div></div>')
    A('</div>')

    A('<div class="verdict reveal">')
    A('<h4>结论:去程 G2921,返程 G2930,高铁全程</h4>')
    A('<p><b>去程选 G2921(10/27 贵阳北 11:14 → 深圳北 15:47,二等座 ¥496.5)</b>。'
      '两天一夜的关键是<b>前一晚必须到深圳</b>:第二天早上 06:30 就要出门过关,'
      '15:47 到深圳北、地铁 4 号线 25 分钟到福田口岸,傍晚就能把干粮买齐、睡个踏实觉。'
      '再晚的 G2945(19:43)和 G2925(23:25)都不行——超市关门、没法采购。'
      '飞机虽然快(1h30-1h50),但要算上提前 2 小时到机场、两地机场往返与摆渡,'
      '总耗时和 4h30 的高铁差不多,票价还贵约 200-500 元。'
      '唯一值得考虑的是早班机 3U1314(07:50 起飞、09:40 到),但当天下午就闲着了,不如省下的钱。')
    A('<p><b>返程选 G2930(10/29 深圳北 14:32 → 贵阳东 19:40,二等座 ¥444.5)</b>。'
      '这一班的时间安排最妙:你们可以<b>从容看完西湾日出</b>,慢悠悠吃个早餐、逛完西湾村,'
      '10:00 前出发都来得及,12:45 到深圳北站还有整整 3 小时余量,'
      '即使 B3X 晚点或口岸排队也不会误车。'
      '17:00 的航班方案虽然到得早,但那意味着 06:25 就要拔营,'
      '把西湾最出彩的日出与星空都浪费在赶路上,而且机票比高铁还贵。')
    A('<p><b>如果想把时间用到极致</b>,返程可以换成 G2922(16:08 发车,¥496.5),'
      '中午还能在西湾村多逛一逛,代价是到贵阳已是晚上 20:32。'
      '想省得最多的组合是 G2921 去 + G2930 回,往返约 <b>¥941</b>。</p>')
    A('<p class="leg-note">'
      '<b>注意</b> · 高铁票价实行市场化浮动,上表为全价参考价,10 月中下旬部分车次有折扣,实际以 12306 下单页为准;'
      '深圳北站客流高峰在 6:00-10:00,建议提前 40 分钟以上到站,开车前 3 分钟停止检票。'
      'D1 早晨的城际交通与 D2 的撤退接送是另一笔账,已含在前面「市内交通」一节。'
      '</p>')
    A('</div></div></section>')

    # 景点详解
    A('<section id="spots"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">01 / THE PLACES</div>'
      '<h2>六个地点,逐一介绍</h2>'
      '<p class="sec-desc">每一处都标了停留时长与补给状况,并附上实拍照片。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="grid g3">')
    for name, en, im1, im2, desc, meta in SPOTS:
        A('<article class="spot reveal">')
        A(f'<div class="spot-img">{img(im1, "", name)}<span class="spot-badge">{en}</span></div>')
        A('<div class="spot-body">')
        A(f'<h3>{name}</h3><div class="spot-en">{en}</div>')
        A(f'<p>{desc}</p>')
        A('<div class="spot-meta">')
        for k, v in meta:
            A(f'<div><dt>{k}</dt><dd>{v}</dd></div>')
        A('</div>')
        A('<div class="tl-media" style="margin-top:14px;border-radius:11px;overflow:hidden">'
          + img(im2, "", name) + '</div>')
        A('</div></article>')
    A('</div></div></section>')

    # 交通
    A('<section id="transit"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">02 / TRANSIT</div>'
      '<h2>去程与返程:打车、大巴还是其他</h2>'
      '<p class="sec-desc">两段路各有三种走法。表格里的时间和费用都按当前实际班次换算,'
      '出发前请再用「香港出行易」复核一次。</p></div>'
      '<div class="rule"></div></div>')

    A('<h3 style="margin:0 0 16px;font-size:19px">去程 · 深圳 → 万宜水库东坝</h3>')
    A('<div class="tbl-wrap reveal"><table><thead><tr>'
      '<th>方案</th><th>路线</th><th>耗时</th><th>费用</th><th>备注</th></tr></thead><tbody>')
    for code, name, tag, route, dur, cost, note in TRANSIT_GO:
        bc = {"推荐": "rec", "最省钱": "eco", "最省心": "easy"}[tag]
        A(f'<tr><td class="t-name"><span class="badge {bc}">{tag}</span>'
          f'<small style="margin-top:6px">{code} · {name}</small></td>'
          f'<td class="t-route">{route}</td><td class="t-time">{dur}</td>'
          f'<td class="t-cost">{cost}</td><td class="t-route">{note}</td></tr>')
    A('</tbody></table></div>')

    A('<h3 style="margin:44px 0 16px;font-size:19px">返程 · 西湾 → 深圳北站(赶 14:32 高铁)</h3>')
    A('<div class="tbl-wrap reveal"><table><thead><tr>'
      '<th>方案</th><th>路线</th><th>耗时</th><th>费用</th><th>备注</th></tr></thead><tbody>')
    for code, name, tag, route, dur, cost, note in TRANSIT_BACK:
        bc = {"推荐,最平衡": "rec", "最省钱": "eco", "若改坐 17:00 航班": "easy",
              "最省心,适合行李多": "easy"}[tag]
        A(f'<tr><td class="t-name"><span class="badge {bc}">{tag}</span>'
          f'<small style="margin-top:6px">{code} · {name}</small></td>'
          f'<td class="t-route">{route}</td><td class="t-time">{dur}</td>'
          f'<td class="t-cost">{cost}</td><td class="t-route">{note}</td></tr>')
    A('</tbody></table></div>')

    A('<div class="two-col" style="margin-top:16px">')
    A('<div class="card mini reveal"><h4>关于「的其他交通工具」</h4>')
    A('<p>除了常规的士与巴士,这条线上还有几样值得知道的:<b>跨境包车</b>(两地牌,'
      '可从香港直达深圳,约 HK$800-1500/车,需提前预约)、<b>跨境渡轮</b>(上环到蛇口,'
      '但从西湾过去太绕)、以及<b>快艇</b>(西湾/咸田湾有到西贡码头的船,旺季每日数班,'
      '单程约 30-160 港币/人,可作为徒步下撤的备选,但不适合赶飞机)。</p>')
    A('<p>另外,<b>港铁东铁线</b>是深港之间最便宜的通道(约 HK$31.8/人),'
      '但从西湾村要绕道西贡与沙田,时间成本高。</p></div>')
    A('<div class="card mini reveal"><h4>过关口岸怎么选</h4>')
    A('<p><b>福田口岸(落马洲支线)</b>:接港铁东铁线,06:30-22:30 开放,最适合公共交通出行者。</p>')
    A('<p><b>皇岗口岸(落马洲管制站)</b>:<b>24 小时开放</b>,是深夜或清晨赶机场的唯一选择,'
      '有皇巴士与跨境出租车往来。</p>')
    A('<p><b>深圳湾口岸</b>:离宝安机场最近,屯门方向有城巴 B3X 直达,适合推荐方案 R1;'
      '实施一地两检,同楼完成两地手续不用下车,旅检开放 06:30-24:00。</p>')
    A('<p>出发前可用香港入境事务处 App 查看各口岸<b>实时轮候时间</b>,绿=少于 15 分钟。</p></div>')
    A('</div></div></section>')

    # 装备
    A('<section id="gear"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">03 / GEAR</div>'
      '<h2>装备清单</h2>'
      '<p class="sec-desc">分三档:缺了就出事的、露营必需的、以及带上会让体验好很多的。</p></div>'
      '<div class="rule"></div></div>')
    A('<div class="grid g3">')
    for title, cls, items in GEAR:
        A(f'<div class="card reveal"><div class="gear-h {cls}"><h3>{title}</h3>'
          f'<span>{"CORE" if cls=="core" else "CAMP" if cls=="camp" else "NICE TO HAVE"}</span></div>')
        A('<div class="gear-list">')
        for t, s in items:
            A(f'<div class="gear-item"><i></i><div><b>{t}</b><small>{s}</small></div></div>')
        A('</div></div>')
    A('</div></div></section>')

    # 警告
    A('<section id="warn"><div class="wrap">')
    A('<div class="sec-head reveal"><div><div class="sec-num">04 / READ THIS FIRST</div>'
      '<h2>出发前必须知道的几件事</h2>'
      '<p class="sec-desc">这一节是全篇最该被认真读完的部分。前两条会直接决定你能不能顺利走完这条线。</p></div>'
      '<div class="rule"></div></div>')
    for title, lvl, body in WARN:
        ic = {"critical": "!", "high": "!", "mid": "i", "good": "✓"}[lvl]
        A(f'<div class="warn {lvl} reveal"><div class="warn-ic">{ic}</div>'
          f'<div><h4>{title}</h4><p>{body}</p></div></div>')
    A('</div></section>')

    # 页脚
    A('<footer><div class="wrap">')
    A('<div class="card reveal" style="background:linear-gradient(150deg,rgba(246,173,85,.09),rgba(79,209,197,.05))">')
    A('<p class="big-q">这条线真正的门槛不在体力,而在<b>信息</b>。'
      '破边洲的预约、露营地的规则、小巴的班次、机场的截载时间——'
      '任何一条信息没核对上,都可能让一整天的计划在早上八点就作废。'
      '出发前把本表再过一遍,并用「香港出行易」和天文台复核当天的班次与天气。</p>')
    A('<p style="font-size:13px;color:var(--mute);margin:0">'
      '本表按 2026 年 10 月 27 日(二)晚抵达深圳、28 日(三)徒步露营、29 日(四)撤回深圳并返程高铁编排,'
      '并已按 4 人同行核算交通费用。路线与班次信息截至 2026 年 10 月。'
      '香港公共交通与营地政策变动频繁,所有时间与费用仅供规划参考,请以当日官方公告为准。</p>')
    A('</div>')
    A('<div class="credits">')
    A('<b>图片来源</b> · 全部照片来自 Wikimedia Commons,经统一调色与压缩后内嵌于本文件:'
      '破边洲与六角岩柱(Underwaterbuffalo、Minghong、rheins、Yumeto、TK HKGP,CC BY-SA 4.0 / CC BY 3.0)、'
      '万宜水库东坝(Underwaterbuffalo、LN9267,CC BY-SA 4.0)、'
      '大浪四湾与西湾(rheins、Kaldari、Thomas H. Brown,CC BY 3.0 / CC0 / CC BY 2.0)、'
      '深圳宝安机场 T3(颠国居,CC BY-SA 4.0)。')
    A('<br><b>资料来源</b> · 香港渔农自然护理署、香港运输署与运输署「香港出行易」、'
      '香港入境事务处、深圳机场集团、深圳市口岸办公室、'
      '以及香港政府新闻公报与多家本地媒体公开报道。')
    A('</div>')
    A('</div></footer>')

    A('''<script>
(function(){
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
  },{threshold:.08,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });
  var secs=[].slice.call(document.querySelectorAll('section[id]'));
  var links=[].slice.call(document.querySelectorAll('.nav-links a'));
  function sync(){
    var y=window.scrollY+120, cur=null;
    secs.forEach(function(s){ if(s.offsetTop<=y) cur=s.id; });
    links.forEach(function(a){
      var on=a.getAttribute('href')==='#'+cur;
      a.style.color=on?'#0a5f54':'';
      a.style.background=on?'rgba(15,123,108,.08)':'';
    });
  }
  window.addEventListener('scroll',sync,{passive:true}); sync();
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('.nav-links a');
    if(a){ document.documentElement.style.scrollBehavior='auto'; }
  });
})();
</script>''')
    A('</body></html>')

    html = "\n".join(P)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print("written:", OUT)
    print("size: %.2f MB" % (os.path.getsize(OUT) / 1024 / 1024))

build()
