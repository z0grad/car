import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Title
st.title('Car Price Prediction\n')



# Load Cleaned Data
df = pd.read_csv('Car_clean.csv')

# Load Preprocessor
preprocessor = pd.read_pickle('preprocessor.pkl')
model = pd.read_pickle('model.pkl')

# Input Data

Brand = st.selectbox('Brand', df['Brand'].unique())
Model = st.selectbox('Model', df['Model'].unique())
Body = st.selectbox('Body', df['Body'].unique())
Color = st.selectbox('Color', df['Color'].unique())
Fuel = st.selectbox('Fuel', df['Fuel'].unique())
Kilometers = st.number_input('Kilometers', df.Kilometers.min(), df.Kilometers.max())
Engine = st.number_input('Engine', df.Engine.min(), df.Engine.max())
Transmission = st.selectbox('Transmission', df['Transmission'].unique())
Gov = st.selectbox('Gov', df['Gov'].unique())
Age_of_Car = st.number_input('Age_of_Car', df.Age_of_Car.min(), df.Age_of_Car.max())

# Preprocessing
new_data = {'Brand': Brand, 'Model': Model, 'Body': Body, 'Color': Color, 'Fuel': Fuel,
         'Kilometers': Kilometers, 'Engine': Engine, 'Transmission': Transmission, 'Gov': Gov, 'Age_of_Car': Age_of_Car}
new_data = pd.DataFrame(new_data, index=[0])
new_data_preprocessed = preprocessor.transform(new_data)


# Prediction
log_price = model.predict(new_data_preprocessed) # in log scale


# Output
if st.button('Predict'):
    st.markdown('# Price Is:')
    st.markdown(log_price)


