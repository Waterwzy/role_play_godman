import math

class GodMan :
    def __init__(self):
        self.god = 0
        self.health = 10
        self.money = 1000
        self.iq = 10
        self.friend = 0
        pass

class EventOfGod :
    def __init__(self , title , description ,require,probability,effect,happenable = False  , last_happen = -math.inf):
        self.title = title#标题
        self.description = description#描述
        self.happenable = happenable#是否可触发
        self.require = require
        '''
        self.require = {
            'event_before' : None,
            'event_time_before' : 0,#之前发生了一定概率后触发
            'event_last_day' : None,#前一天发生了一定概率后触发
            'state_required' : None,#在一定阶段触发
            'god_require' : -math.inf,#各种神人值的需要条件
            'health_require' : -math.inf,
            'money_require' : -math.inf,
            'iq_require' : -math.inf,
            'friend_require' : -math.inf,

        }
        '''
        self.last_happen = last_happen#上次触发事件
        self.probability = probability#概率值
        self.effect = effect
        '''
        self.effect = {
            'god' : 0,
            'health' : 0,
            'money' : 0,
            'iq' : 0,
            'friend' : 0,
        }
        '''
        pass