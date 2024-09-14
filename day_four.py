import random

class Card(object):
    """一张牌"""
    
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face
    
    @property
    def face(self):
        return self._face
    
    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]    #列表的生成表达式语法 - 相当于正常的for循环嵌套(笛卡尔积)
        self._current = 0
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        """洗牌(随机乱序)"""

        self._current = 0
        random.shuffle(self._cards)
    
    @property
    def next(self):
        """发牌"""

        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """是否还有牌"""

        return self._current < len(self._cards)

class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name
    
    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""

        self._cards_on_hand.append(card)
    
    def arrange(self, card_key):
        """玩家整理手上的牌"""

        self._cards_on_hand.sort(key=card_key)


#排序规则 - 先根据花色在根据点数排序
def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ') 
        player.arrange(get_key)
        print(player.cards_on_hand)



"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
        
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0
    
class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour
    
class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales    

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0
    
    def get_salary(self):
        return 1200.0 * self._sales * 0.05

def main():
    emps = [Manager('刘备'), Programmer('赵云'),
            Manager('曹操'), Salesman('夏侯惇'),
            Salesman('吕布'), Programmer('诸葛亮'),
            Programmer('关云长')]
    
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间:' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额:' % emp.name))
        print('%s本月工资为:￥%s元' % (emp.name, emp.get_salary()))