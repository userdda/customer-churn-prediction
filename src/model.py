import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score

def train_and_evaluate(data_path="../data/processed_users.csv"):
    # 加载数据
    df = pd.read_csv(data_path)

    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Logistic Regression
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train_scaled, y_train)
    y_pred_lr = log_reg.predict(X_test_scaled)

    print("逻辑回归")
    print("Accuracy:", accuracy_score(y_test, y_pred_lr))
    print("Recall:", recall_score(y_test, y_pred_lr))

    # Random Forest
    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    print("\n随机森林")
    print("Accuracy:", accuracy_score(y_test, y_pred_rf))
    print("Recall:", recall_score(y_test, y_pred_rf))

if __name__ == "__main__":
    train_and_evaluate()
