from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import os

def prepare_data():
    os.makedirs('ml/data', exist_ok=True)
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names

    # v1数据（原始）
    data_v1 = pd.DataFrame(X, columns=feature_names)
    data_v1['target'] = y
    data_v1.to_csv('ml/data/iris_v1.csv', index=False)

    # v2数据（大幅增加噪声）
    np.random.seed(42)
    data_v2 = data_v1.copy()
    
    # 对所有特征添加显著噪声
    for i in range(4):  # 所有4个特征
        noise = np.random.normal(0, 1.0, size=len(data_v1))  # 噪声标准差增加到1.0
        data_v2.iloc[:, i] += noise
    
    data_v2.to_csv('ml/data/iris_v2.csv', index=False)
    print("数据重新生成完成")

if __name__ == "__main__":
    prepare_data()
    