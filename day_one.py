from math import sqrt
from random import randint

def is_prime():
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


def calculate_num():
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break


def print_graph():
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()


    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


def find_Narcissistic_number():
    for num in range(100,1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def reverse_num():
    num = int(input('请输入一个整数:'))
    reverse_num = 0
    while num > 0:
        reverse_num = reverse_num * 10 + num % 10
        num //= 10
    print(reverse_num)


def dollars_and_chicken():
    for x in range(0 , 20):
        for y in range(0 , 33):
            z = 100 - x - y
            if x * 5 + y * 3 + z / 3 == 100:
                print('%d只公鸡, %d只母鸡, %d只小鸡' % (x , y , z))


def GRAPS():
    money = 1000
    while money > 0:
        print('你的总资产:', money)
        need_go_on = False
        while True:
            debt = int(input('请下注:'))
            if 0 < debt <= money:
                break
        first = randint(1,6) + randint(1,6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt     
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt 
        else:
            need_go_on = True
        while need_go_on:
            need_go_on = False
            current = randint(1,6) + randint(1,6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜!')
                money -= debt
            elif current == first:
                print('玩家胜!')
                money += debt
            else:
                need_go_on = True
    print('你破产了,游戏结束!')


def perfect():
    for num in range(2, 10000):
        result = 0
        for factor in range(1, int(sqrt(num)) + 1):
            if num % factor == 0:
                result += factor
                if factor > 1 and num // factor != factor:
                    result += num // factor
        if result == num:
            print(num)
