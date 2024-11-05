import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

# The input array must match the feature order that the model was trained on. 
# For example, if the model was trained with features in the order 
# ["class", "dp", "astv", "mean", "altv", "mode", "median", "ac", "variance", "mstv"], 
# then you must pass them in that exact order when making a prediction.

st.title('Classifying Fetal State')
st.markdown('Toy model to play to classify fetal state into normal, suspect, or pathological')

st.header("CTG Diagnostic Features")
class_ = st.slider('Class', 1, 10, 1)
dp = st.number_input("DP",value=0)
astv = st.number_input("ASTV",value=0)
mean = st.number_input("Mean",value=0)
altv = st.number_input("ALTV",value=0)
mode = st.number_input("Mode",value=0)
median = st.number_input("Median",value=0)
ac = st.number_input("AC",value=0)
variance = st.number_input("Variance",value=0)
mstv = st.number_input("MSTV",value=0)

# It's a good practice to document your features and their respective indices or orders, 
# so that anyone reading your code can understand which variable corresponds to which feature.
        
features = {
    "class": class_,
    "dp": dp,
    "astv": astv,
    "mean": mean,
    "altv": altv,
    "mode": mode,
    "median": median,
    "ac": ac,
    "variance": variance,
    "mstv": mstv
}

st.text('')
if st.button('Predict the state of fetus'):
    result = predict(
        np.array([[features["class"], features["dp"], features["astv"], features["mean"], 
                             features["altv"], features["mode"], features["median"], 
                             features["ac"], features["variance"], features["mstv"]]]))
    st.text(result[0])

#'CLASS', 'DP', 'ASTV', 'Mean', 'ALTV', 'Mode', 'Median', 'AC', 'Variance', 'MSTV'
