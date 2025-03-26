import numpy as np
import matplotlib.pyplot as plt

def generate_coin_sequence(n_flips, p_head=0.08):
    """生成硬币序列，1表示正面，0表示反面
    
    参数:
        n_flips (int): 抛硬币的总次数
        p_head (float): 硬币正面朝上的概率，默认为0.08
        
    返回:
        ndarray: 一个长度为n_flips的一维数组，其中1表示正面，0表示反面
    """
    return np.random.choice([0, 1], size=n_flips, p=[1-p_head, p_head])

def calculate_waiting_times(coin_sequence):
    """计算两次正面之间的等待时间（反面次数）
    
    参数:
        coin_sequence (ndarray): 硬币序列，1表示正面，0表示反面
        
    返回:
        ndarray: 一个数组，包含所有等待时间（即连续两次正面之间的反面次数）
    """
    heads_indices = np.nonzero(coin_sequence == 1)[0]
    if len(heads_indices) < 2:
        return np.array([])
    return np.diff(heads_indices) - 1

def plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=None):
    """绘制等待时间直方图
    
    参数:
        waiting_times (ndarray): 等待时间数组
        log_scale (bool): 是否使用对数坐标，默认为False
        n_flips (int, optional): 抛硬币总次数，用于标题显示
    """
    plt.figure()
    plt.hist(waiting_times, bins=50, density=True, alpha=0.7, log=log_scale)
    
    title = "Waiting Time Distribution"
    if n_flips:
        title += f" (n={n_flips})"
    if log_scale:
        title += " (log scale)"
    
    plt.title(title)
    plt.xlabel("Number of Tails between Heads")
    plt.ylabel("Probability Density")
    plt.grid(True, alpha=0.3)
    plt.show()

def analyze_waiting_time(waiting_times, p_head=0.08):
    """分析等待时间的统计特性
    
    参数:
        waiting_times (ndarray): 等待时间数组
        p_head (float): 硬币正面朝上的概率，默认为0.08
        
    返回:
        dict: 包含统计量的字典
    """
    if len(waiting_times) == 0:
        return {
            "mean": 0,
            "std": 0,
            "theoretical_mean": (1-p_head)/p_head,
            "exponential_mean": 1/p_head
        }
    
    return {
        "mean": np.mean(waiting_times),
        "std": np.std(waiting_times),
        "theoretical_mean": (1-p_head)/p_head,
        "exponential_mean": 1/p_head
    }

def run_experiment(n_flips, title, p_head=0.08):
    """运行一次等待时间实验
    
    参数:
        n_flips (int): 抛硬币的总次数
        title (str): 实验标题
        p_head (float): 硬币正面朝上的概率，默认为0.08
        
    返回:
        tuple: (waiting_times, stats)
    """
    print(f"\n=== {title} ===")
    
    # 生成序列并计算等待时间
    sequence = generate_coin_sequence(n_flips, p_head)
    waiting_times = calculate_waiting_times(sequence)
    
    # 分析统计特性
    stats = analyze_waiting_time(waiting_times, p_head)
    print(f"平均等待时间: {stats['mean']:.2f} (理论值: {stats['theoretical_mean']:.2f})")
    print(f"标准差: {stats['std']:.2f}")
    
    # 绘制直方图
    if len(waiting_times) > 0:
        plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=n_flips)
        plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=n_flips)
    else:
        print("警告: 没有足够的正面来计算等待时间")
    
    return waiting_times, stats

if __name__ == "__main__":
    # 设置随机种子以保证可重复性
    np.random.seed(42)
    
    # 任务一：1000次抛掷
    waiting_times_1k, stats_1k = run_experiment(1000, "Task 1: 1000 Coin Flips")
    
    # 任务二：1000000次抛掷
    waiting_times_1m, stats_1m = run_experiment(1000000, "Task 2: 1,000,000 Coin Flips")
