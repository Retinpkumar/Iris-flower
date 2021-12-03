import joblib

def input_scalar(input_dataframe):
    scalar_filepath = 'saved_files/data/standard_scaler.sav'
    scalar = joblib.load(scalar_filepath)
    scaled_dataframe = scalar.transform(input_dataframe)
    return scaled_dataframe
