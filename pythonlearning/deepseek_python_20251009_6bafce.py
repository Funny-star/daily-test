import os
import time
import random
import msvcrt
from enum import Enum

# 游戏方向枚举
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# 游戏类
class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]  # 蛇的初始位置
        self.direction = Direction.RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        
    def generate_food(self):
        """生成食物位置"""
        while True:
            food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if food not in self.snake:
                return food
    
    def draw(self):
        """绘制游戏界面"""
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏
        
        # 绘制上边界
        print('+' + '-' * (self.width * 2) + '+')
        
        for i in range(self.height):
            print('|', end='')
            for j in range(self.width):
                if (i, j) == self.snake[0]:
                    print('@', end=' ')  # 蛇头
                elif (i, j) in self.snake:
                    print('O', end=' ')  # 蛇身
                elif (i, j) == self.food:
                    print('*', end=' ')  # 食物
                else:
                    print(' ', end=' ')  # 空白
            print('|')
        
        # 绘制下边界
        print('+' + '-' * (self.width * 2) + '+')
        print(f'得分: {self.score} | 使用WASD控制方向，Q退出游戏')
        
        if self.game_over:
            print('游戏结束!')
    
    def update(self):
        """更新游戏状态"""
        if self.game_over:
            return
        
        # 获取蛇头位置
        head_i, head_j = self.snake[0]
        
        # 根据方向计算新的蛇头位置
        if self.direction == Direction.UP:
            new_head = (head_i - 1, head_j)
        elif self.direction == Direction.DOWN:
            new_head = (head_i + 1, head_j)
        elif self.direction == Direction.LEFT:
            new_head = (head_i, head_j - 1)
        elif self.direction == Direction.RIGHT:
            new_head = (head_i, head_j + 1)
        
        # 检查是否撞墙或撞到自己
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width or 
            new_head in self.snake):
            self.game_over = True
            return
        
        # 移动蛇
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()  # 如果没有吃到食物，移除蛇尾
    
    def change_direction(self, new_direction):
        """改变蛇的方向"""
        # 防止直接反向移动
        if (new_direction == Direction.UP and self.direction != Direction.DOWN or
            new_direction == Direction.DOWN and self.direction != Direction.UP or
            new_direction == Direction.LEFT and self.direction != Direction.RIGHT or
            new_direction == Direction.RIGHT and self.direction != Direction.LEFT):
            self.direction = new_direction

# 主游戏循环
def main():
    game = SnakeGame()
    
    print("贪吃蛇游戏")
    print("使用 WASD 控制方向")
    print("按任意键开始游戏...")
    msvcrt.getch()  # 等待按键
    
    while not game.game_over:
        game.draw()
        game.update()
        
        # 非阻塞键盘输入
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'q':
                break
            elif key == 'w':
                game.change_direction(Direction.UP)
            elif key == 's':
                game.change_direction(Direction.DOWN)
            elif key == 'a':
                game.change_direction(Direction.LEFT)
            elif key == 'd':
                game.change_direction(Direction.RIGHT)
        
        time.sleep(0.2)  # 控制游戏速度
    
    game.draw()  # 显示最终结果

if __name__ == "__main__":
    main()