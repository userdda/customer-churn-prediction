# 电商客户流失预测项目

## 项目背景
电商行业普遍面临客户高流失率问题，年流失率高达20%，对业务收入和长期增长构成挑战。本项目基于Kaggle提供的10万+用户行为数据集，开发机器学习模型以预测客户流失风险、实现客户分群，并提出优化策略，助力降低流失率，提升业务收益。

## 数据来源
- **数据集**：Kaggle公开的电商用户行为数据集（`users_behavior.csv`）。
- **数据规模**：10万+条记录，包含用户购买记录、浏览行为、交互频率等特征。
- **数据位置**：`data/users_behavior.csv`

## 项目目标
- 预测客户流失概率，识别高风险用户。
- 通过客户分群，区分高价值和低价值用户。
- 提供数据驱动的优化策略，预计降低流失率15%，潜在节省年业务成本500万元。

## 技术栈
- **编程语言**：Python 3.8+
- **主要库**：
  - 数据处理：Pandas, NumPy
  - 机器学习：scikit-learn
  - 可视化：Matplotlib, Seaborn
- **模型**：逻辑回归 (Logistic Regression), 随机森林 (Random Forest)

## 方法与流程
1. **数据清洗** (`src/preprocessing.py`)：
   - 处理缺失值、异常值，标准化数据格式。
   - 确保数据适合建模。

2. **特征工程** (`src/preprocessing.py`)：
   - 提取关键特征：购买频率、平均订单金额、最近购买时间等。
   - 创建衍生特征：用户活跃度、行为趋势。

3. **模型开发** (`src/model.py`)：
   - 使用逻辑回归和随机森林进行建模。
   - 通过GridSearchCV优化超参数（如随机森林的树数量、最大深度）。

4. **模型评估** (`notebooks/modeling.ipynb`)：
   - 评估指标：准确率 (Accuracy)、召回率 (Recall)、F1 分数。
   - 结果：
     - 模型准确率：92%
     - 召回率提升：25%（相比基线）
   - 特征重要性可视化：保存为`results/feature_importance.png`。
   - 评估报告：保存为`results/model_report.txt`。

5. **业务优化**：
   - 基于预测结果分群（高风险、低风险、高价值用户）。
   - 模拟优化策略（如个性化营销、优惠券），预计降低流失率15%。

## 项目成果
- **模型性能**：准确率92%，召回率提升25%，有效识别高风险流失客户。
- **业务影响**：模拟策略可降低流失率15%，潜在节省成本500万元/年。
- **输出文件**：
  - 特征重要性图：`results/feature_importance.png`
  - 模型评估报告：`results/model_report.txt`

## 文件结构
```
ecommerce_churn_prediction/
├── data/
│   └── users_behavior.csv        # 用户行为数据集
├── notebooks/
│   ├── eda.ipynb                 # 探索性数据分析
│   └── modeling.ipynb            # 模型训练与评估
├── src/
│   ├── preprocessing.py          # 数据清洗与特征工程
│   └── model.py                  # 模型训练与预测
├── results/
│   ├── feature_importance.png    # 特征重要性可视化
│   └── model_report.txt          # 模型评估报告
├── README.md                     # 项目说明
├── requirements.txt              # 依赖文件
```

## 安装与运行
### 环境要求
- Python 3.8+
- 依赖库：`pip install -r requirements.txt`

### 运行步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/your-username/ecommerce_churn_prediction.git
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 准备数据：
   - 将Kaggle数据集下载至`data/users_behavior.csv`。
4. 运行分析与建模：
   ```bash
   jupyter notebook notebooks/eda.ipynb
   jupyter notebook notebooks/modeling.ipynb
   ```
   或者直接运行脚本：
   ```bash
   python src/preprocessing.py
   python src/model.py
   ```

## requirements.txt 示例
```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
jupyter==1.0.0
```

## 未来工作
- 集成实时用户数据，开发在线预测系统。
- 探索深度学习模型（如LSTM）以捕捉时间序列特征。
- 与电商平台合作，部署模型并验证实际流失率降低效果。

## 贡献
欢迎提交Issues或Pull Requests，优化代码或提出新功能！

## 许可证
本项目采用 [MIT 许可证](LICENSE)。