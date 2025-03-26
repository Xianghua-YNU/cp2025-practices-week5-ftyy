import matplotlib.pyplot as plt
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 包含x和y坐标序列的元组 (x_coords, y_coords)
    """
    # TODO: 实现随机行走算法
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 分别生成x和y方向的步长序列
    # 3. 使用 cumsum() 计算累积和得到轨迹
    # 生成随机步长
    # 生成x和y方向的随机步长（-1或1)
    x_steps = np.random.choice([-1, 1], size=steps)
    y_steps = np.random.choice([-1, 1], size=steps)
    
    # 计算累积和得到轨迹坐标（从原点(0,0)开始）
    x_coords = np.cumsum(x_steps)
    y_coords = np.cumsum(y_steps)
    
    # 在开头插入原点(0,0)
    #x_coords = np.insert(x_coords, 0, 0)
    #y_coords = np.insert(y_coords, 0, 0)
    
    return x_coords, y_coords
def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (tuple): 包含x和y坐标序列的元组
    """
    # TODO: 实现单个轨迹的绘制
    # 提示：
    # 1. 使用 plt.plot 绘制轨迹线
    # 2. 使用 plt.scatter 标记起点和终点
    # 3. 设置坐标轴比例相等
    # 4. 添加图例
    x, y = path
    
    plt.figure(figsize=(8, 8))
    # 绘制轨迹线
    plt.plot(x, y, alpha=0.7, lw=1, label='Trajectory')
    # 标记起点和终点
    plt.scatter(x[0], y[0], c='green', s=100, label='Start (0, 0)')
    plt.scatter(x[-1], y[-1], c='red', s=100, label=f'End ({x[-1]}, {y[-1]})')
    
    plt.title('2D Diagonal Random Walk (1000 Steps)')
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.show()

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    # TODO: 实现多个轨迹的绘制
    # 提示：
    # 1. 创建2x2的子图布局
    # 2. 对每个子图重复以下步骤：
    #    - 生成随机行走轨迹
    #    - 绘制轨迹线
    #    - 标记起点和终点
    #    - 设置标题和图例
    plt.figure(figsize=(12, 12))
    
    for i in range(4):
        # 生成随机行走轨迹
        x, y = random_walk_2d(1000)
        
        # 选择子图位置
        plt.subplot(2, 2, i+1)
        # 绘制轨迹
        plt.plot(x, y, alpha=0.7, lw=1)
        # 标记起点和终点
        plt.scatter(x[0], y[0], c='green', s=50, label='Start')
        plt.scatter(x[-1], y[-1], c='red', s=50, label='End')
        
        # 设置子图标题和标签
        plt.title(f'Trajectory {i+1}\nEnd: ({x[-1]}, {y[-1]})')
        plt.xlabel('X position')
        plt.ylabel('Y position')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.axis('equal')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # TODO: 完成主程序逻辑
    # 1. 生成并绘制单个轨迹
    # 2. 生成并绘制多个轨迹
    # 生成并绘制单个轨迹
    print("Generating single random walk...")
    single_path = random_walk_2d(1000)
    plot_single_walk(single_path)
    
    # 2. 生成并绘制4个不同的轨迹（1000步）
    print("Generating multiple random walks for comparison...")
    plot_multiple_walks()
