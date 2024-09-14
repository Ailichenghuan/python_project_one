import pygame
from random import randint
from collision_detection import Color, Ball



def main():
    # 定义用来装所有球的容器
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10,10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、颜色和速度随机)
                ball = Ball(x, y, radius, sx, sy,color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球，如果没被吃掉就绘制，被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50ms就改变球的位置在刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()