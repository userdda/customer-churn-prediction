# Customer Churn Prediction

📌 本项目旨在预测电商客户流失，帮助企业降低流失率、提升用户留存。  

## 数据
- 数据来源：[Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- 规模：模拟 100k+ 用户记录  

## 方法
- 数据清洗与特征工程（Pandas、Scikit-learn）
- 模型：逻辑回归 & 随机森林
- 评估指标：准确率、召回率、F1-score、ROC AUC  

## 结果
- 模型准确率达 **92%**
- 召回率提升 **25%**
- 模拟优化策略可降低流失率 **15%**
- 业务模拟：潜在节省成本 ~ **500万/年**

## 运行方式
```bash
pip install -r requirements.txt
python src/train.py

customer-churn-prediction/
│── data/                # 存放样例数据（小规模CSV）
│── notebooks/           # Jupyter Notebook 实验记录
│── src/                 # 核心代码
│   ├── preprocessing.py # 数据清洗与特征工程
│   ├── train.py         # 模型训练脚本
│   ├── evaluate.py      # 评估与指标
│── requirements.txt     # 依赖库
│── README.md            # 项目说明
│── results/             # 保存结果图表/模型指标
