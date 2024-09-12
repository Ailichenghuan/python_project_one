import os
import time

def main():
    content = '锁王来到了交通大学'
    while True:
        os.system('cls')
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]

"""
if __name__ == '__main__':
    main()
"""


import random

def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename,has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]

    return m1, m2
    
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    days_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],
                     [31,29,31,30,31,30,31,31,30,31,30,31]
                     ][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

"""
if __name__ == '__main__':
    main()

"""


def yanghui_Triangle():
    num = int(input('Number of rows:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] *(row+1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end='\t')

        print()


from random import randrange, randint, sample

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end='')
    print()

def random_select():
    red_balls = [x for x in range(1,34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))

def main():
    n = int(input('机选几注:'))
    for _ in range(n):
        display(random_select())


def main():
    """
    约瑟夫环的公式:f(M, N) = (f(M - 1, N) + 3) % M 
    """
    persons = [True] * 30
    counter, index, number = 0, 0, 0    #counter - 代表被kill的人数，index - 代表被kill的人的索引位置(循环)，number - 代表需要被kill的人(每9个kill一个)
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基'if person else '非', end='')


import os

def print_board(board):
    print(board['LU'] + '|' + board['UM'] + '|' + board['RU'])
    print('-+-+-')
    print(board['LM'] + '|' + board['MM'] + '|' + board['RM'])
    print('-+-+-')
    print(board['LD'] + '|' + board['MD'] + '|' + board['RD'])

def main():
    init_board = {
        'LU':' ', 'UM':' ', 'RU':' ',
        'LM':' ', 'MM':' ', 'RM':' ',
        'LD':' ', 'MD':' ', 'RD':' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋,请输入位置:' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局?(yes/no)')
        begin = choice == 'yes'