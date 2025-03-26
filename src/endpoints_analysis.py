import numpy as np
import matplotlib.pyplot as plt

def random_walk_finals(num_steps, num_walks):
    """生成多个二维随机游走的终点位置
    
    通过模拟多次随机游走，每次在x和y方向上随机选择±1移动，
    计算所有随机游走的终点坐标。每个随机游走都从原点(0,0)开始。

    参数:
        num_steps (int): 每次随机游走的步数
        num_walks (int): 随机游走的次数
        
    返回:
        tuple: 包含两个numpy数组的元组 (x_finals, y_finals)
            - x_finals: 所有随机游走终点的x坐标数组，长度为num_walks
            - y_finals: 所有随机游走终点的y坐标数组，长度为num_walks
            
    示例:
        >>> x_finals, y_finals = random_walk_finals(1000, 100)
        >>> print(f"第一个终点坐标: ({x_finals[0]}, {y_finals[0]})")
    """
    # TODO: 实现随机游走算法
    # 提示：
    # 1. 使用np.zeros初始化坐标数组
    # 2. 对每次游走使用np.random.choice生成±1的随机步长
    # 3. 使用np.sum计算总位移
    x_finals = np.zeros(num_walks)
    y_finals = np.zeros(num_walks)
    
    for i in range(num_walks):
        x_steps = np.random.choice([-1, 1], num_steps)
        y_steps = np.random.choice([-1, 1], num_steps)
        
        x_finals[i] = np.sum(x_steps)
        y_finals[i] = np.sum(y_steps)
    
    return x_finals, y_finals

def plot_endpoints_distribution(endpoints):
    """绘制二维随机游走终点的空间分布散点图
    
    将多次随机游走的终点在二维平面上可视化，观察其空间分布特征。
    图形包含所有终点的散点图，并保持x和y轴的比例相同。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> plot_endpoints_distribution(endpoints)
        >>> plt.show()
    """
    # TODO: 实现散点图绘制
    # 提示：
    # 1. 使用endpoints解包获取x和y坐标
    # 2. 使用plt.scatter绘制散点图
    # 3. 设置坐标轴比例、标题和标签
    x_coords, y_coords = endpoints
    
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("2D Random Walk Endpoints")
    plt.xlabel("xlabel")
    plt.ylabel("ylabel")

def analyze_x_distribution(endpoints):
    """分析二维随机游走终点x坐标的统计特性
    
    对随机游走终点的x坐标进行统计分析，计算样本均值和样本方差，
    并通过直方图和理论正态分布曲线可视化其分布特征。理论上，
    大量随机游走的终点x坐标应该服从正态分布。

    参数:
        endpoints: 包含x和y坐标的元组 (x_coords, y_coords)
            - x_coords: numpy数组，所有终点的x坐标
            - y_coords: numpy数组，所有终点的y坐标
    
    返回:
        tuple: (mean, variance)
            - mean (float): x坐标的样本均值
            - variance (float): x坐标的样本方差（使用n-1作为分母）
            
    示例:
        >>> endpoints = random_walk_finals(1000, 1000)
        >>> mean, var = analyze_x_distribution(endpoints)
        >>> print(f"均值: {mean:.2f}, 方差: {var:.2f}")
    """
    # TODO: 实现统计分析和可视化
    # 提示：
    # 1. 提取x坐标数据
    # 2. 使用numpy计算均值和方差
    # 3. 绘制直方图
    # 4. 添加理论正态分布曲线
    # 5. 设置图形属性并打印统计结果
    x_coords, _ = endpoints
    
    # 计算均值和方差
    mean = np.mean(x_coords)
    variance = np.var(x_coords, ddof=1)
    
    # 绘制直方图
    plt.hist(x_coords, bins=30, density=True, alpha=0.6, color='g')
    
    # 绘制正态分布曲线
    from scipy.stats import norm
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, np.sqrt(variance))
    plt.plot(x, p, 'k', linewidth=2)
    
    plt.title("x coordinate distribution and theoretical normal distribution")
    plt.xlabel("xlabel")
    plt.ylabel("PDF")
    
    print(f"均值: {mean:.2f}, 方差: {variance:.2f}")

if __name__ == "__main__":
    np.random.seed(42)  # 设置随机种子以保证可重复性
    
    # 生成数据
    endpoints = random_walk_finals(1000, 1000)

    # 创建图形
    plt.figure(figsize=(12, 5))
    
    # 绘制终点分布
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 分析x坐标分布
    plt.subplot(122)
    analyze_x_distribution(endpoints)
    
    plt.tight_layout()
    plt.show()
