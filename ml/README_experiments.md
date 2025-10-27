#experimental records
# 实验记录

##Experiment 1: Baseline model (v1 data)
-Data version: v1 (raw iris data)
-Model: Random forest (n_estimators=100)
-Accuracy: ~ 0.95-1.0
## 实验1：基线模型（v1数据）
- 数据版本：v1（原始鸢尾花数据）
- 模型：随机森林（n_estimators=100）
- 准确率：约0.95-1.0

##Experiment 2: Improved model (v2 data)
-Data version: v2 (noisy data)
-Model: Random forest (n_estimators=100)
-Accuracy: ~ 0.9-0.95
## 实验2：改进模型（v2数据）
- 数据版本：v2（添加噪声的数据）
- 模型：随机森林（n_estimators=100）
- 准确率：约0.9-0.95

##Production Readiness Model 
Select ** Experiment 1 (baseline model)** as production model because: 
- Use raw data (v1) Higher accuracy
-cleaner data, no artificially added noise
-Optimized metrics: Accuracy (most important for classification problems) 
## 生产就绪模型选择
选择**实验1（基线模型）**作为生产模型，因为：
- 使用原始数据（v1）准确率更高
- 数据更干净，没有人为添加的噪声
- 优化指标：准确率（对分类问题最重要）

##Test Notes
- Iris dataset is small and simple, and the model easily achieves 100% accuracy
- Data version difference testing should focus on changes in the data itself, rather than forcing performance differences
- This reflects the robustness of the model to data changes
## 测试注意事项
- 鸢尾花数据集较小且简单，模型容易达到100%准确率
- 数据版本差异测试应关注数据本身的变化，而非强制要求性能差异
- 这反映了模型对数据变化的鲁棒性
