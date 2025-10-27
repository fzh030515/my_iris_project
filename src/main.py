import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn
import argparse
import os

def load_data(version='v1'):
    """加载指定版本的数据集"""
    if version not in ['v1', 'v2']:
        raise ValueError("Invalid data version. Use 'v1' or 'v2'.")
    
    try:
        if version == 'v1':
            data_path = 'ml/data/iris_v1.csv'
        else:
            data_path = 'ml/data/iris_v2.csv'
        
        data = pd.read_csv(data_path)
        feature_columns = [col for col in data.columns if col not in ['target', 'target_name']]
        return data, feature_columns
    except FileNotFoundError as e:
        print(f"Error: Data file not found: {e}")
        return None, None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def train_model(data_version='v1', random_state=42):
    """训练模型并记录实验"""
    if data_version not in ['v1', 'v2']:
        raise ValueError("Invalid data version. Use 'v1' or 'v2'.")
    
    data, feature_columns = load_data(version=data_version)
    if data is None:
        print("Failed to load data")
        return 0
    
    X = data[feature_columns]
    y = data['target']
    
    # 分割数据
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state
    )
    
    # 开始MLflow运行
    with mlflow.start_run():
        # 记录参数
        mlflow.log_param("data_version", data_version)
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_param("test_size", 0.2)
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", random_state)
        
        # 训练模型
        model = RandomForestClassifier(n_estimators=100, random_state=random_state)
        model.fit(X_train, y_train)
        
        # 预测和评估
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        
        # 记录指标
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision_avg", report['macro avg']['precision'])
        mlflow.log_metric("recall_avg", report['macro avg']['recall'])
        
        # 创建输入示例（解决MLflow第二个警告）
        input_example = X_train.iloc[:1]
        
        # 记录模型（已修复第一个警告，添加输入示例解决第二个警告）
        mlflow.sklearn.log_model(
            model, 
            name="iris_model",
            input_example=input_example  # 添加输入示例
        )
        
        print(f"Model trained with data {data_version}")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
        
        return accuracy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train Iris classifier.')
    parser.add_argument('--data-version', type=str, default='v1', help='Dataset version: v1 or v2')
    parser.add_argument('--random-state', type=int, default=42, help='Random state for reproducibility')
    args = parser.parse_args()
    
    train_model(data_version=args.data_version, random_state=args.random_state)
    