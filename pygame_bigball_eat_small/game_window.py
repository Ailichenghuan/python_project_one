import pygame

def main():
    #初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800 ,600))
    # 设置当前窗口标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
if __name__ == '__main__':
    main()