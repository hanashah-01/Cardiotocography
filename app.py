import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

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

st.text('')
if st.button('Predict the state of fetus'):
    result = predict(
        np.array([[class_, dp, astv, mean, altv, mode, median, ac, variance, mstv]]))
    st.text(result[0])

#'CLASS', 'DP', 'ASTV', 'Mean', 'ALTV', 'Mode', 'Median', 'AC', 'Variance', 'MSTV'