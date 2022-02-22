import numpy as np


def forget_miu(data, forgot_factor=0.99):
    ans = 0
    # input a 1*n sample vector
    for i in range(len(data) - 1, -1, -1):
        ans = data[i] + forgot_factor * ans
    return ans


def forget_fenmu(data, forgot_factor=0.99):
    ans = 0
    for i in range(len(data)):
        ans = forgot_factor * ans + forgot_factor
    return ans


def forgot_cov(wjc_data, forgot_factor=0.1):
    # 每行代表一个随机变量，包含若干个sample

    # 为每个元素加入遗忘因子
    forgot_data = np.zeros(wjc_data.shape)
    for i in range(forgot_data.shape[0]):
        for j in range(forgot_data.shape[1]):
            forgot_data[i][j] = wjc_data[i][j] * forgot_factor ** (forgot_data.shape[1] - j - 1)
    # print(forgot_data)

    # 每行减去自己的平均值
    for i in range(len(wjc_data)):
        mid_raw_mean = np.mean(wjc_data[i])
        for j in range(len(wjc_data[i])):
            wjc_data[i][j] = wjc_data[i][j] - mid_raw_mean
    # 计算cov
    cov_denomitor = forget_fenmu(forgot_data[0])
    X = np.array(forgot_data)

    print('cov', X.dot(X.T) / cov_denomitor)
    return X.dot(X.T) / cov_denomitor


wjc_data = np.array([[0.04, 0.02, -0.1, -0.05],
                     [0.03, 0.04, -0.09, 0.02],
                     [0.03, 0.04, -0.09, 0.02]])
forgot_cov(wjc_data)
