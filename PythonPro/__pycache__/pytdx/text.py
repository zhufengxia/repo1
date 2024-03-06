# 来源：https://blog.csdn.net/weixin_43704656/article/details/120921289
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
df = pd.read_csv(r"D:\Tencent\WeChat\WeChat Files\wxid_8lxs4geol41w22\FileStorage\File\2024-01\上证指数2.csv")
# print(df.head())
# 用调整后的收盘价 Adj Close来预测股价，首先取出数据保存到x0中，用values属性把它转成numpy形式，len(x0)看下x0有多少个数据
# 我这里直接用收盘价
x0 = df['close'].values
print(f"x0.shape={x0.shape}")
# 接下来对数据做预处理，我们希望每个数据都介于0-1之间，方便我们做预测
# 首先我们去除x0中最大的数据，之后所有的数据都与最大数据做除法
m = max(x0)
print(f"max is {m}")
x0 = x0 / m
print(x0[:10])
''' n代表有多少个数据，p代表以20个数据预测下一个值 
x是训练数据的一部分 从k到k+p，k是从总数量中减去p再加1取'''
n = len(x0)
p = 20  # 以20个数据预测下一个值
x = np.array([x0[k:k + p] for k in range(n - p + 1)])
# x0[k:k + p]：切片操作，获取从索引 k 到索引 k + p - 1（不包括 k + p）的子数组。
print(f"x.shape={x.shape}")
print(x)
y = np.array(x0[p:])
# x0[p:] 表示从索引 p 开始到末尾的所有元素
print(f"y.shape={y.shape}")
print(y)
# y.shape()看到y比x少一个数据，因为前20个数据才预测出一个y
"""有相同个数据，方便接下来预测 
因为keras读入的数据有三个维度，这里我们给x加上一个新的维度，方便keras读取数据
X.shape()可以看到X变成了三维的数据
"""
X = x[:-1]
X = X[:, :, np.newaxis]
print(f"X.shape={X.shape}")
"""做训练和预测，
test_size = 0.2 表示 20%的数据做训练，80%的数据做预测
shuffle=True，让数据重新洗过（当shuffle设置为False时，可以发现预测效果差很多）"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
"""train_test_split 是一个常用的函数，用于将数据集随机划分成训练集和测试集。
它的参数包括输入数据（通常是特征矩阵 X）和对应的输出数据（通常是目标向量 y），
以及指定测试集大小的参数 test_size。通过设置 test_size 的值（0.2），可以指定测试集在整个数据集中所占比例。
shuffle=True 参数表示在划分数据集之前是否对数据进行洗牌（随机打乱顺序）。
这样可以保证训练集和测试集的分布是随机的，避免因数据的有序性导致模型训练结果的偏差。
X_train 和 y_train 存储了划分后的训练集数据，而 X_test 和 y_test 存储了划分后的测试集数据。
"""

"""接下来进行模型搭建，主要用到的是keras中的Sequential来搭建
下面是搭建模型用到的一些包，这里用到一维的卷积，一维的最大池化，优化器我这里导入了两个，可以分别尝试下看看预测效果
Dense全连接网络
Flatten可以把二维数据摊成一维
Dropout防止过拟合
Activate激活函数"""
from keras.models import Sequential
from keras.layers import Dense, Flatten, Reshape, Dropout, Activation
from keras.layers import Conv1D, MaxPooling1D
from keras.optimizers import SGD
from keras.optimizers import Adam

# 模型搭建较为简单，只有三层。一维的卷积层、最大池化层、摊平数据之后连接了一个全连接网络。
# 激活函数这里用到的是sigmoid。（softmax通常用在分类问题上，我们今天的数据类似于回归问题，所以这里使用sigmoid）
# 模型搭建
model = Sequential()
# 50个filter卷积核 学习到更多的特征，same保证维度不变
model.add(Conv1D(50, 4, padding='same', activation='relu', input_shape=(p, 1)))
"""50: 这表示该卷积层会输出 50 个不同的滤波器（filter），也就是说它会检测输入数据中的 50 个不同特征。
4: 这是指定了卷积核的大小，也就是滤波器的宽度。在一维卷积中，这个值表示滤波器的长度。
padding='same': 这表示在卷积操作中使用零填充（zero padding），以保持输入和输出的长度相同。
activation='relu': 这表示在卷积操作后应用 ReLU 激活函数。
input_shape=(p, 1): 这定义了输入数据的形状，其中 p 表示输入数据的长度，1 表示输入数据的通道数（在这里是一维数据）。"""
model.add(MaxPooling1D(2))  # 每两个取一个大的   数据会减少一半
model.add(Flatten())  # 把二维数据变成一维的
model.add(Dense(20))  # 20个神经元的全连接层
model.add(Dropout(0.2))  # 防止过拟合 20%权重冻结
model.add(Activation('relu'))
model.add(Dense(1))  # 输出层 是一个一维的全连接神经网络
model.add(Activation('sigmoid'))
# model.compile(loss='mse',optimizer=SGD(lr=0.2), metrics['accuracy'])
model.compile(loss='mse', optimizer=SGD(lr=0.2))
model.summary()
# 下面开始训练模型，用到model.fit()这个函数
model.fit(X_train, y_train, epochs=50, batch_size=32)
# 指定保存模型的文件路径和名称
model.save('my_model.h5')
# 保存模型权重
model.save_weights('my_model_weights.h5')
y_predict = model.predict(X_test)
plt.plot(y_test[:100])  # 取前一百个  真实数据
plt.plot(y_predict[:100], 'r')  # 模型学到的
plt.show()  # 显示图形
