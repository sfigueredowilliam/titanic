import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import accuracy_score
import joblib

# Carregando o Dataset Titanic
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
dados = pd.read_csv(url)

print(dados.columns)

dados = dados.drop(columns=["Name"])

# Remove valores ausentes
dados = dados.dropna(subset=["Age", "Fare"])

# Convertendo variáveis categóricas
dados = pd.get_dummies(dados, columns=["Sex", "Pclass"], drop_first=True)

X = dados.drop(columns="Survived")
y = dados["Survived"]
# Separando os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

# Criando e treinando modelo XGBoost
modelo = xgb.XGBClassifier(objective="binary:logistic", eval_metric="logloss")
modelo.fit(X_train, y_train)

# Fazendo previsões
preds = modelo.predict(X_test)

# Avaliando o modelo
acuracia = accuracy_score(y_test, preds)
print(f"A acurácia do modelo é: {acuracia:.2%}")

# Salvando o modelo treinado
joblib.dump(modelo, "model_titanic.pkl")