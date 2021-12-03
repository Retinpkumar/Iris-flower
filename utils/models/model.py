import joblib

model_path = "saved_files/data/model.sav"
model = joblib.load(model_path)

def predict(attribues):
    prediction = model.predict(attribues)
    return prediction
