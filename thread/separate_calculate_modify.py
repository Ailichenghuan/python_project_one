from multiprocessing import Process, Queue
from random import randint
from time import time

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动八个进程将数据切片后运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time:', (start - end), 's',sep='')
    # sep参数是用来设定print()中的多个对象之间的连接符号是什么，默认是空格，而print中多个对象之间是通过逗号，来分隔。

if __name__ == '__main__':
    main()