import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split # pour diviser le jeu de données initial en 1 jeu d'entrainement (X_train, y_train) et un jeu de test (X_test, y_test)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import r2_score, mean_squared_error

def test():
    return "test"

def train():
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    # df_original = pd.read_csv("données d'origine.csv")
    df_original = pd.read_csv("data_cleaned_cheated.csv")
    df = df_original[['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges', 'charges_group_cheat']]

    df['group'] = np.where(df['charges'] < 4746.344000, '1', 
                                np.where(df['charges'] < 9386.161300, '2', 
                                np.where(df['charges'] < 16657.717450, '3', '4')))

    # df = df[df['charges'] < 49000]
    # df_group['group'] = np.where(df_group['charges'] < 4719.736550, '1', 
                                #  np.where(df_group['charges'] < 9301.893550, '2', 
                                #  np.where(df_group['charges'] < 16297.846000, '3', '4')))

    mapping_sex = {'male': 0, 'female': 1}
    mapping_smoker = {'yes': 1, 'no': 0}

    # df['sex'] = df['sex'].map(mapping_sex)
    # df['smoker'] = df['smoker'].map(mapping_smoker)
    df['northeast'] = 0
    df['southeast'] = 0
    df['northwest'] = 0
    df['southwest'] = 0
    df.loc[df['region'] == 'northeast', 'northeast'] = 1
    df.loc[df['region'] == 'southeast', 'southeast'] = 1
    df.loc[df['region'] == 'northwest', 'northwest'] = 1
    df.loc[df['region'] == 'southwest', 'southwest'] = 1

    df.loc[:, 'smoker_bmi'] = df['smoker'] * df['bmi']
    df.loc[:, 'smoker_age'] = df['smoker'] * df['age']
    df.loc[:, 'charges_group'] = np.where(df['smoker'] == 0, 1,
                                        np.where(df['bmi'] >= 30, 3,
                                                np.where(df['sex'] == 0, 2,
                                                            np.where(df['age'] < 22, 1, 3))))
    df.loc[:, 'diff_charges_group'] = abs(df['charges_group'] - df['charges_group_cheat'])
    df['children'] = np.where(df['children'] > 0, 1, 0) 

    # nettoyage
    df = df[['age', 'sex', 'bmi', 'children', 'smoker', 'smoker_bmi', 'smoker_age', 'northeast', 'southeast', 'northwest', 'southwest', 'charges', 'charges_group_cheat', 'diff_charges_group', 'charges_group', 'group']]

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ### PolynomialFeatures ###
    ##########################

    y = df[['charges']]
    X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'smoker_bmi', 'northeast', 'southeast', 'northwest', 'southwest']] # southeast
    X = df[['age', 'bmi', 'children', 'smoker', 'smoker_bmi', 'charges_group']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.85, random_state=42, stratify=X['smoker'])

    X_train_robust = RobustScaler().fit_transform(X_train)

    #creer variables polynomiales a partir de nos variables
    X_poly = PolynomialFeatures(2).fit_transform(X_train_robust)
    X_poly_robust = RobustScaler().fit_transform(X_poly)

    # Crée le modèle de régression linéaire
    model = LinearRegression()

    # Entraîne le modèle sur les données d'entraînement
    model.fit(X_poly, y_train)

    # Faire des prédictions sur les données d'entraînement
    predictions_train = model.predict(X_poly_robust)

    # Calcule le R^2 et l'erreur quadratique moyenne (MSE) sur les données d'entraînement
    r2_train = r2_score(y_train, predictions_train)
    mse_train = mean_squared_error(y_train, predictions_train)
    rmse_train = np.sqrt(mse_train)

    print(f"R^2 Score (Train): {r2_train}")
    # print(f"MSE (Train): {mse_train}")
    # print(f"RMSE (Train): {rmse_train}")

    return "Le modèle est entrainé."