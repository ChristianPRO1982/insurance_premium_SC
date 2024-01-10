from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, RobustScaler, OneHotEncoder
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.compose import ColumnTransformer
import pandas as pd

#importe le csv
df = pd.read_csv('insurance_dataset.csv')

train, test = train_test_split(df, test_size=0.2, random_state=42) #divise données en 80/20
X_train = train[['age', 'smoker', 'bmi', 'children']] #[[liste de noms de colonnes]]
                
#X_train_encoded = pd.get_dummies(X_train, columns=['region'], prefix='region')]] #X_train est une matrice avec les données explicatives numériques

X_train = train[['age', 'smoker', 'bmi', 'children']] #[[liste de noms de colonnes]]
y_train = train['charges']

X_test = test[['age', 'smoker', 'bmi', 'children']]
y_test = test['charges']

model = make_pipeline (PolynomialFeatures(), RobustScaler(), Lasso())

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

params = {'polynomialfeatures__degree': [1,2,3]}

grid = GridSearchCV(model, param_grid=params, cv =4)

grid.fit(X_train, y_train)


r2_test = r2_score(y_test, y_pred)
mse_test = mean_squared_error(y_test, y_pred)
rmse_test = mean_squared_error(y_test, y_pred, squared=False)
print(f"R^2 Score (Test): {r2_test}")
print(f"MSE (Test): {mse_test}")
print(f"RMSE (Test): {rmse_test}")

print (y_pred)