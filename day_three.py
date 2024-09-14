from time import sleep

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """
        时钟初始化
        
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """

        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """时钟走表"""

        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
        
    def show(self):
        """显示时间"""

        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

def main():
    clock = Clock(23,59,48)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        """初始化
        :param x: 横坐标
        :param y: 纵坐标
        """

        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x:新的横坐标
        :param y:新的纵坐标 
        """

        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        坐标移动的增量
        :param dx:横坐标增量 
        :param dy:纵坐标增量
        """

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离 
        :param other: 另一个点
        """

        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)
    
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
    
def main():
    p1 = Point(1, 3)
    p2 = Point(2, 5)
    print(p1)
    print(p2)
    p2.move_to(-1, 2)
    print(p2)
    print(p1.distance_to(p2))
    p1.move_by(-1, 2)
    print(p1)
    print(p1.distance_to(p2))



from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta): 
    """战斗者"""

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0
    
    @abstractmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技:必打掉对方%50或者四分之三的血量"""

        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
        
    def magic_attack(self, others):
        """
        魔法攻击
        :param others:被攻击的群体 
        """

        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False
        
    def resume(self):
        """回复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    
    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
        '生命值：%d\n' % self._hp + \
        '魔法值：%d\n' % self._mp

class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
        '生命值：%d\n' % self._hp
    
def is_any_alive(monsters):
        for monster in monsters:
            if monster.alive > 0:
                return True
        return False

def select_alive_one(monsters):
        monsters_len = len(monsters)
        while True:
            index = randrange(monsters_len)
            monster = monsters[index]
            if monster.alive > 0:
                return monster
    
def display_info(ultraman, monsters):
        print(ultraman)
        for monster in monsters:
            print(monster, end='')
    
def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('赛博坦星人', 500)
    m2 = Monster('哥斯拉', 750)
    m3 = Monster('基多拉', 250)
    ms = [m1, m2, m3]

    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=======第%02d回合=======' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)  #通过随机数选择使用哪种技能
        if skill <= 6:          #%60的概率使用普攻
            print('%s使用魔法攻击打了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点' % (u.name, u.resume()))
        elif skill <= 9:        #%30的概率使用魔法攻击，但是可能会因为魔法不足而失败
            if u.magic_attack(ms):
                print('%s使用了魔法攻击', u.name)
            else:
                print('%s使用魔法攻击失败' % u.name)
        else:                   #%10的概率使用必杀技，如若魔法不足则使用普通攻击
            if u.huge_attack(m):
                print('%s使用了奥特光线射击了%s' % (u.name, m.name))
            else:
                print('%s用普通攻击打了%s' % (u.name, m.name))
                print('%s魔法恢复了%d点' % (u.name, u.resume()))
        if m.alive > 0:       #被选中的怪兽没死就回击奥特曼
            print('%s回击了%s' % (m.name, u.name))
            m.attack(u)

        display_info(u, ms)
        fight_round += 1
    print('\n=======战斗结束!=======')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')