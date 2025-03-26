import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def plot_poisson_pmf(lambda_param=8, max_l=20):
    """绘制泊松分布的概率质量函数
    
    参数:
        lambda_param (float): 泊松分布参数λ
        max_l (int): 最大的l值
    """
    # TODO: 实现泊松分布概率质量函数的计算和绘制
    # 提示：
    # 1. 使用np.arange生成l值序列
    # 2. 使用给定公式计算PMF
    # 3. 使用plt制图形并设置标签
    # 生成l值的序列
    l_values = np.arange(0, max_l+1)
    
    # 计算泊松分布PMF
    pmf_values = (lambda_param ** l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    # 绘制PMF图形
    plt.plot(l_values, pmf_values, 'bo', label=f'λ = {lambda_param}')
    plt.title("poisson pmf")
    plt.xlabel("l")
    plt.ylabel("P(X=l)")
    plt.xticks(l_values)
    plt.grid(True)
    plt.legend()

def simulate_coin_flips(n_experiments=10000, n_flips=100, p_head=0.08):
    """模拟多组抛硬币实验
    
    参数:
        n_experiments (int): 实验组数N
        n_flips (int): 每组抛硬币次数
        p_head (float): 正面朝上的概率
        
    返回:
        ndarray: 每组实验中正面朝上的次数
    """
    # TODO: 实现多组抛硬币实验
    # 提示：
    # 1. 使用np.random.choice模拟硬币抛掷
    # 2. 统计每组实验中正面的次数
    flips = np.random.choice([0, 1], size=(n_experiments, n_flips), p=[1-p_head, p_head])
    
    # 统计每组实验中正面朝上的次数
    heads_count = np.sum(flips, axis=1)
    
    return heads_count

def compare_simulation_theory(n_experiments=10000, lambda_param=8):
    """比较实验结果与理论分布
    
    参数:
        n_experiments (int): 实验组数
        lambda_param (float): 泊松分布参数λ
    """
    # TODO: 实现实验结果与理论分布的对比
    # 提示：
    # 1. 调用simulate_coin_flips获取实验结果
    # 2. 计算理论分布
    # 3. 绘制直方图和理论曲线
    # 4. 计算并打印统计信息
    # 获取模拟的实验结果
    heads_count = simulate_coin_flips(n_experiments=n_experiments, n_flips=100, p_head=0.08)
    
    # 计算实验中正面朝上的次数分布的直方图
    plt.hist(heads_count, bins=30, density=True, alpha=0.6, color='g', label='模拟结果')
    
    # 计算泊松分布的理论PMF
    max_l = np.max(heads_count)
    l_values = np.arange(0, max_l+1)
    pmf_values = (lambda_param ** l_values * np.exp(-lambda_param)) / factorial(l_values)
    
    # 绘制理论泊松分布曲线
    plt.plot(l_values, pmf_values, 'bo-', label=f'泊松分布，λ={lambda_param}')
    
    # 设置图形属性
    plt.title("实验结果与泊松分布的对比")
    plt.xlabel("正面朝上的次数")
    plt.ylabel("概率密度")
    plt.legend()
    plt.grid(True)

if __name__ == "__main__":
    # 设置随机种子
    np.random.seed(42)
    
    # 1. 绘制理论分布
    plot_poisson_pmf()
    
    # 2&3. 进行实验模拟并比较结果
    compare_simulation_theory()
    
    plt.show()
