import streamlit as st
import pandas as pd
from utils.models.model import predict
from utils.models.scalar import input_scalar

# page settings
st.set_page_config(page_title="Iris Flower Predictor App",
                   page_icon="🌺",
                   layout="centered")

# page header
st.title(f"Iris Flower Predictor App")

with st.form("Prediction_form"):
    # form header
    st.header("Enter the flower specifications:")
    # input elements
    sepal_length = st.number_input(label="Sepal Length: ", min_value=0.0, max_value=10.00, step=0.01)
    sepal_width = st.slider(label="Sepal Width: ", min_value=0.0, max_value=5.00, step=0.01)
    petal_length = st.number_input(label="Petal Length: ", min_value=0.0, max_value=10.00, step=0.01)
    petal_width = st.slider(label="Petal Width: ", min_value=0.0, max_value=5.00, step=0.01)
    # submitt values
    submit_values = st.form_submit_button("Predict")

if submit_values:
    # create input dictionary
    input_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    # create input dataframe
    input_dataframe = pd.DataFrame(input_dict, index=[1])
    # scale inputs
    input_scaled = input_scalar(input_dataframe)
    # make predictions
    prediction = predict(input_scaled)

    if prediction == 0:
        value = 'Setosa'
    elif prediction == 1:
        value = 'Versicolour'
    else:
        value = 'Virginica'

    # output header
    st.header("Here is the prediction: ")
    # output results
    st.success(f'The flower is: "Iris-{value}" ')
    # balloons..
    st.balloons()
