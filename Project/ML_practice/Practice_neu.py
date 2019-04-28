## 参考：http://python.jobbole.com/82758/
import numpy as np


# sigmoid function
def nonlin(x, deriv=False):  # deriv 斜率
    if (deriv == True):
        return x * (1 - x)  # 若Sigmoid的输出值用变量out表示，则其导数值可简单通过式子out *(1-out)得到，这是非常高效的。
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])  # 我们的神经网络便有 3 个输入节点，4 个训练实例。

# output dataset
y = np.array([[0, 0, 1, 1]]).T
# “.T” 为转置函数。经转置后，该  y  矩阵便包含 4 行 1 列。网络含有 3 个输入， 1 个输出

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)
# 随机数设定产生种子是一个良好的习惯。
# 这样一来，你得到的权重初始化集仍是随机分布的，
# 但每次开始训练时，得到的权重初始集分布都是完全一致的。这便于观察你的策略变动是如何影响网络训练的。

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1  # random.random()用于生成用于生成一个指定范围内的随机符点数
# 实现了该神经网络权重矩阵的初始化操作。用 “syn0” 来代指 “零号突触”（即“输入层-第一层隐层”间权重矩阵）。
# 只需要一个权重矩阵来连接它们。权重矩阵维度为（3,1），是因为神经网络有 3 个输入和 1 个输出。
# 也就是 l0 层大小为 3 ， l1 层大小为 1 。

for iter in range(10000):  # 2.x xrange 3.x range
    # for循环迭代式地多次执行训练代码，使得我们的网络能更好地拟合训练集。

    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))  # dot 矩阵相乘操作
    # 前向预测阶段。基本上，首先让网络基于给定输入“试着”去预测输出。
    # 代码包含两个步骤。首先，将l0与syn0进行矩阵相乘。然后，将计算结果传递给sigmoid函数。具体考虑到各个矩阵的维度：
    # (4 x 3)dot(3 x 1) = (4 x 1)

    # how much did we miss?
    l1_error = y - l1
    # 反映出网络的误差有多大

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)
    # 重中之重（核心部分）

    # update weights
    syn0 += np.dot(l0.T, l1_delta)  # dot 矩阵相乘操作
    # 更新权值
    # 首先计算每一个训练实例中每一个权值对应的权值更新量（有正负之分），再将每个权值的所有更新量累加起来，接着更新这些权值。

print("Output After Training:")
print(l1)