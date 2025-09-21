# 电商客户流失预测

## 项目概述
本项目针对电商行业高流失率问题（年流失率约20%）进行分析和建模。基于Kaggle提供的超过10万条用户行为数据集，开发机器学习模型以分析客户行为、实现客户分群并预测流失风险，旨在提供可操作的洞察以降低流失率并优化客户留存策略。

## 主要成果
- **数据分析与预处理**：使用Python（Pandas、scikit-learn）进行数据清洗和特征工程，为建模准备高质量数据。
- **建模**：采用逻辑回归和随机森林模型进行客户流失预测和用户行为分群。
- **结果**：
  - 模型准确率达到**92%**。
  - 召回率提升**25%**，显著改善了对高风险客户的识别。
  - 模拟优化策略可将流失率降低**15%**，预计每年为业务节省**500万美元**成本。

## 仓库结构
```
ecommerce_churn_prediction/
├── data/
│   └── users_behavior.csv        # 用户行为数据集（Kaggle）
├── notebooks/
│   ├── eda.ipynb                # 探索性数据分析笔记本
│   └── modeling.ipynb           # 模型训练与评估笔记本
├── src/
│   ├── preprocessing.py         # 数据清洗与特征工程脚本
│   └── model.py                 # 模型训练与预测脚本
├── results/
│   ├── feature_importance.png   # 特征重要性可视化
│   └── model_report.txt         # 模型性能报告
├── README.md                    # 项目文档
├── requirements.txt             # 所需的Python依赖包
```

## 安装步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/your-username/ecommerce_churn_prediction.git
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 确保数据集（`users_behavior.csv`）已放置在`data/`目录下。

## 使用方法
1. **探索性数据分析**：
   - 运行`notebooks/eda.ipynb`以探索数据集并可视化用户行为的关键模式。
2. **数据预处理**：
   - 使用`src/preprocessing.py`进行数据清洗和特征工程。
3. **模型训练与评估**：
   - 运行`notebooks/modeling.ipynb`以训练逻辑回归和随机森林模型，并评估其性能。
   - 查看`results/model_report.txt`获取详细的模型性能指标，查看`results/feature_importance.png`了解关键特征。

## 依赖项
主要使用的库：
- Python 3.8+
- Pandas
- scikit-learn
- Jupyter Notebook
- Matplotlib/Seaborn（用于可视化）

完整依赖列表见`requirements.txt`。

## 未来工作
- 引入更多算法（如XGBoost、神经网络）以提升模型性能。
- 集成实时数据管道以实现动态流失预测。
- 扩展特征工程，纳入外部数据源（如人口统计或交易数据）。

## 贡献
欢迎贡献代码！请提交拉取请求或开启议题以提供建议或改进。

## 许可证
本项目采用MIT许可证。