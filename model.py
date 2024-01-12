import joblib

def predict(data):
    pred = joblib.load('model.sav')
    return pred.predict(data)