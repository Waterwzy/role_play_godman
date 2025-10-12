from main import EventOfGod
import random
import math
import time
random.seed(time.time())

god_list = []
#title , description ,require,probability,happenable = False  , last_happen = -math.inf
god_list.append(EventOfGod(
    '哲学时间' ,
    'StarredMate025在群内大谈特谈自己的哲学观点（当然是错误的），被群友指出错误后无力反驳但坚持自己的观点',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    30,
    {
        'god': 20,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': random.randint(-3,-5),
    }
))
god_list.append(EventOfGod(
    '天外横财',
    'StarredMate025得到了一笔意外财富（奶奶的养老钱），并且决定将其用于“追逐梦想”',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    40,
    {
        'god': 40,
        'health': 0,
        'money': random.randint(2000,3500),
        'iq': 0,
        'friend': 0,
    }
))
god_list.append(EventOfGod(
    '母慈子孝',
    '由于StarredMate025多次取走奶奶的养老钱并且用于“追逐梦想”，奶奶和他断绝了关系。',
    {
        'event_before': '天外横财',
        'event_time_before': random.randint(3,5),  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    math.inf,
    {
        'god': 40,
        'health': 0,
        'money': random.randint(2000,3500),
        'iq': 0,
        'friend': 0,
    }
))#special effect
god_list.append(EventOfGod(
    '无能の⭐⭐',
    'StarredMate025在工作中碰见了一个已婚的丰腴貌美的少妇女上司，觉得StarredMate025势力微弱，人才济济，想与StarredMate025啪啪啪',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': 10,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    9.1,
    {
        'god': 91,
        'health': -random.randint(78,91)/10,
        'money': 0,
        'iq': 0,
        'friend': random.randint(20,30),
    },
    last_happen= 3
))
god_list.append(EventOfGod(
    '数码之王',
    'StarredMate025在网络上发现了极为便宜的免费硬件，并大肆宣扬可以500元组装3A游戏负载的强度极高电脑，并且想拼装5080S的属于自己的电脑，但是最终发现他给的配置就是石。',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': 3000,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    38,
    {
        'god': 15,
        'health': 0,
        'money': -random.randint(500,2000),
        'iq': 0,
        'friend': -random.randint(20,30),
    }
))
god_list.append(EventOfGod(
    '万国开战',
    '大开聊天群，在噼里啪啦大量发布小广告，混进一批成分不明人物，任人唯亲，甚至有些不属于圈内人。',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    14,
    {
        'god': 20,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': -random.randint(20,40),
    }
))
god_list.append(EventOfGod(
    '哲学の讨论（单方面）',
    'StarredMate025在与deepseek的深度讨论中悟得哲学真谛，并向群友们探讨（尽管没有人想和他讨论这玩意儿）',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    70,
    {
        'god': 25,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': -5,
    }
))
god_list.append(EventOfGod(
    '王者内战',
    'StarredMate025每天带着群友们去干一些不属于这个群的事情。',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    20,
    {
        'god': 15,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': -10,
    }
))
god_list.append(EventOfGod(
    '你的帽子怎么尖尖的',
    '跟ai搏斗了一个晚上',
    {
        'event_before': '舌战群儒',
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    91,
    {
        'god': 99,
        'health': -20,
        'money': 0,
        'iq': 0,
        'friend': -20,
    }
))
god_list.append(EventOfGod(
    '幻想时间',
    '又幻想了，幻想自己积累原始资本，幻想更换劳动工具，幻想自己开车送外卖',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    50,
    {
        'god': 20,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': 0,
    }
))
god_list.append(EventOfGod(
    '舌战群儒',
    'StarredMate025在夜间偶遇来辨论的三人与之展开辩论最终不敌',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': 2,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    50,
    {
        'god': 30,
        'health': 0,
        'money': 0,
        'iq': 0,
        'friend': 0,
    }
))#special effect
god_list.append(EventOfGod(
    'xdm找到工作了-其一',
    'StarredMate025似乎找到了一份工作：外卖员',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    25,
    {
        'god': 0,
        'health': 0,
        'money': 3000,
        'iq': 0,
        'friend': 0,
    }
))#special effect
god_list.append(EventOfGod(
    'xdm找到工作了-其二',
    'StarredMate025似乎找到了一份工作（？）：船员',
    {
        'event_before': None,
        'event_time_before': 0,  # 之前发生了一定概率后触发
        'event_last_day': None,  # 前一天发生了一定概率后触发
        'state_required': None,  # 在一定阶段触发
        'god_require': -math.inf,  # 各种神人值的需要条件
        'health_require': -math.inf,
        'money_require': -math.inf,
        'iq_require': -math.inf,
        'friend_require': -math.inf,
    },
    25,
    {
        'god': 0,
        'health': 0,
        'money': 3000,
        'iq': 0,
        'friend': 0,
    }
))#special effect