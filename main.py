import math
import init_event

event_list=[]

class GodMan :
    def __init__(self):
        self.god = 0
        self.health = 100
        self.money = 1000
        self.iq = 100
        self.friend = 100
        pass

class EventOfGod :
    def __init__(self , title , description ,require,probability,effect,happenable = True  , last_happen = -math.inf):
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

def had_done(list_happened:list[str],target_event:str) :
    count = 0
    for event in list_happened:
        if target_event == event:
            count += 1
    return count

def select_list(even_list:list[EventOfGod],state:int,man:GodMan,list_happened:list[str]) :
    available_list = []
    for event in even_list:
        if event.require['state_required'] is not None and state != event.require['state_required']:
            continue
        if event.require['event_last_day'] is not None and list_happened[-1] == event.require['event_last_day'] :
            continue
        if event.require['event_before'] is not None and had_done(list_happened,event.require['event_before'])>=event.require['event_time_before'] :
            continue
        if event.require['god_require'] > man.god or event.require['health_require'] > man.health or event.require['money_require'] > man.money or event.require['iq_require'] > man.iq or event.require['friend_require'] > man.friend :
            continue
        available_list.append(event)
    return available_list

def choose_event(available_list:list[EventOfGod]) :
    weigh = []
    for event in available_list:
        weigh.append(event.probability)
    
    return

if __name__ == "__main__" :
    event_happened = []
    event_list = init_event.create_god_list()
    state = 1#第一阶段
    SM = GodMan( )

    while True :
        available = select_list(event_list,state,SM,event_happened)