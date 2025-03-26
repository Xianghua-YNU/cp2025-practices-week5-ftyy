import numpy as np
import matplotlib.pyplot as plt

def random_walk_displacement(num_steps, num_simulations):
    """
    模拟随机行走并返回每次模拟的最终位移

    参数:
    num_steps (int): 随机行走的步数
    num_simulations (int): 模拟的次数

    返回:
    numpy.ndarray: 形状为(2, num_simulations)的数组，表示每次模拟的最终位移
    """
    # TODO: 检查输入参数的有效性
    if num_steps < 1 or num_simulations < 1:
        raise ValueError("num_steps和num_simulations必须大于0")
    # TODO: 实现随机行走算法
    random_steps = np.random.choice([-1, 1], size=(2, num_simulations, num_steps))
    final_displacements = random_steps.sum(axis=2)
    return final_displacements
    # 提示：
    # 1. 使用 np.random.choice 生成随机步长 ([-1, 1])
    # 2. 生成形状为 (2, num_simulations, num_steps) 的数组
    # 3. 对步数维度求和得到最终位移
    


def plot_displacement_distribution(final_displacements, bins=30):
    """
    绘制位移分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移分布的直方图绘制
    # 1. 计算每次模拟的最终位移
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    displacements = np.sqrt(final_displacements[0]**2 + final_displacements[1]**2)
    plt.hist(displacements, bins=bins, density=True, alpha=0.7, color='g')
    plt.title("Displacement Distribution")
    plt.xlabel("Displacement")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def plot_displacement_square_distribution(final_displacements, bins=30):
    """
    绘制位移平方分布直方图

    参数:
    final_displacements (list): 包含每次模拟最终位移的列表
    bins (int): 直方图的组数
    """
    # TODO: 实现位移平方分布的直方图绘制
    # 1. 计算位移平方
    # 2. 使用plt.hist绘制直方图
    # 3. 添加标题和标签
    displacements = np.sqrt(final_displacements[0]**2 + final_displacements[1]**2)
    plt.hist(displacements**2, bins=bins, density=True, alpha=0.7, color='b')
    plt.title("Displacement Square Distribution")
    plt.xlabel("Displacement Square")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # 可调整的参数
    num_steps = 1000  # 随机行走的步数
    num_simulations = 1000  # 模拟的次数
    bins = 30  # 直方图的组数

    # TODO: 完成主程序逻辑
    # 1. 调用random_walk_displacement获取模拟结果
    # 2. 绘制位移分布直方图
    # 3. 绘制位移平方分布直方图
    final_displacements = random_walk_displacement(num_steps, num_simulations)
    plot_displacement_distribution(final_displacements, bins)
    plot_displacement_square_distribution(final_displacements, bins)
    
