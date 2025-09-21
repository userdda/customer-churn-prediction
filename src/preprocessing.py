import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(input_path="../data/users_behavior.csv",
                    output_path="../data/processed_users.csv"):
    # 读取原始数据
    df = pd.read_csv(input_path)

    # 删除明显无用的字段（如用户ID）
    if "user_id" in df.columns:
        df = df.drop(columns=["user_id"])

    # 填补缺失值
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].fillna("Unknown")

    # 类别编码
    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    # 保存处理后的数据
    df.to_csv(output_path, index=False)
    print(f"数据清洗完成，已保存至 {output_path}")

if __name__ == "__main__":
    preprocess_data()
