import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

st.set_page_config(layout= 'wide')
data = pd.read_csv('Car_clean.csv')
 
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Uesd Car in Egypt')
with row0_2:
    st.text("")
    st.subheader('App by [Ahmed ELSaied](https://www.linkedin.com/in/ahmed-el-saied-75ab56217/)')
    st.subheader('Prediction Price [Prediction](http://localhost:8502/)')

row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("This project aims to predict typical bus costs in Egypt, so that buyers can make an informed purchasing decision using data collected from colorful sources spread across colorful areas in Egypt. We realize that buses are not just a means of transportation, but an expression of our own tastes and needs. The choice may be limited depending on our budget, however, we can take advantage of regular car demand to enjoy the luxury brands we love at lower prices. By examining the available data, we will provide information about the cost of manned buses based on the brand, model, condition and other dependent factors. This will enable buyers to make an informed purchasing decision and choose a vehicle that suits their requirements and budget. .")
    st.markdown("You can find the source code in the [Uesd Car in Egypt GitHub Repository](https://github.com/ahmedsaeed620/Used-Car-Price-in-Egypt.git)")

### Understanding Data ###
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data = st.expander('You can click here to see the raw data first ')
    with see_data:
        st.dataframe(data=data.reset_index(drop=True))
    st.text('')

### Univariate Categorical variables ###
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('Analysis Univariate For Categorical Variables ')
row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row5_1:
    st.markdown('Any value in Every Column of E-Commerce Is More in Demand?')    
    option = st.selectbox('selsect an option' , ['Brand', 'Model', 'Body', 'Color', 'Fuel', 'Transmission', 'Gov'],key ="option_sec1") 
    st.markdown('brand ---> most popular is Htheyundai')
    st.markdown('Model ---> The most popular model is the Verna')
    st.markdown('Body ---> most popular is Sedan')
    st.markdown('Color ---> most popular is Black')
    st.markdown('Fuel ---> It is natural that Benzine is the most, because natural gas is one of the types that appeared recently')
    st.markdown('Transmission ---> With the continuous development in the world of cars, automatic cars are modern and help trainees to drive well, while manual cars are the basis for driving education, so it is natural that they are the most popular.')

with row5_2:
    fig = px.bar(data[option].value_counts() ,text_auto='0.3s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)
    st.markdown('Gov ---> Given that Cairo is the capital of Egypt and the center of life services in it, as it has the largest number of families among the population, it is natural that the governorates use the most cars. ')  
    

### Univariate Numerical Variables ###
row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    st.subheader('Analysis Univariate Numerical Variables')
row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row7_1:
    st.markdown('In Which Range Numaric Value Lies, What Is Distribution Look Like?')    
    option1 = st.selectbox('selsect an option' , ['Kilometers', 'Engine', 'Price', 'Age_of_Car'],key = "tap_sec2")   
with row7_2:
    fig = px.histogram(data_frame= data , x = option1 )
    st.plotly_chart(fig)

### Analysis Bivariate Categorical Variables ###
row9_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
    st.subheader('Analysis Bivariate  Categorical Variables')
row10_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row9_1:
    st.markdown('Is there a significant relationship between a (Categorical variables)and their likelihood to churn?')    
    option = st.selectbox('selsect an option' , ['Brand', 'Model', 'Body', 'Color', 'Fuel', 'Transmission', 'Gov'],key = "tap_sec4")
    st.markdown('brand ---> Hyundai cars are the highest.')
    st.markdown('model ---> Although the most-produced car in the dataset is the Verna, it represents the lowest average price and the Tipo is the most-produced.')


with row9_2:
 option_price = data.groupby(option)['Price'].mean().sort_values(ascending=False)
 fig = px.bar(option_price , color = option_price.index )
 st.plotly_chart(fig)



### Analysis Bivariate Numerical Variables ###
row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
with row10_1:
    st.subheader('Analysis Bivariate  Numerical Variables')
row11_spacer1, row11_1, row11_spacer2, row11_2, row11_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row11_1:
    st.markdown('Does the (Numerical Values) have a significant impact on their likelihood to churn?')    
    option1 = st.selectbox('selsect an option' , ['Kilometers', 'Engine', 'Age_of_Car'],key = "tap_sec5")  
    st.markdown('Kilometers --->It is natural for the relationship to be inverse, because with an increase in car traffic, it leads to a decrease in their prices')
    st.markdown('Engine ---> there is a direct relationship that when the Engine increases, the price of the car increases')
    st.markdown('Age_of_Car --->  the relationship is inverse, because the age of the car has increased and it has become old, so its price is cheap')

with row11_2:
    fig = px.scatter(data , x = (data[option1]),y= (data['Price'])) 
    st.plotly_chart(fig)

row11_spacer1, row11_1, row11_spacer2 = st.columns((.2, 7.1, .2))
with row11_1:
    st.subheader('Important Features')
row12_spacer1, row12_1, row12_spacer2, row12_2, row12_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row12_1:
    st.markdown('The biggest impact is the age of the car, which determines its depreciation over time')
    st.markdown('And also the effect of transportation Effective in a way that approaches the life of the car , Model, brand, Kilometers')

with row12_2:
    image_url ='https://www.kaggleusercontent.com/kf/142898563/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..yVTCKUkYgGDekkbZGyWDPg.tcNfAF6SLrHdj1PLUqYJBkvjTCeS4DFT04YIP7K01FwyCyfqVlf6NMQL3XgumfrULWEnp6EEzVsLIxXEO7n_2phBQLcT35SPvGEfqEUADcikzbL9j-JTFMXZDAS2i0pKrsT1ZFyVl8dcGYO78jRlb6FXjrBtq0TvpHkj61o-tkT3pPO3Mbs5Gp-DbwCSMI8Xm88619L-v5tHwYJTT-U5z3o9_utclKq2SPgkh3Gg09p11sD-ULZrP9ndl38ZcPrTkPbvU-tr-qvRAQD_TH57j-1ni9jbIfm2BqtntuG7y3uvbiUq6o-iLuBp523O0Iv_EgJsuMsuH4cY3k__Vc-BuHGhgdJOPLJv0c5ZoJjlOHe0NH1nXIFocvSXFzhmXbOIk9PdmkJphclrig-uQ93fOZv56uuC59E6aOArMxMNnKxjF-ImXAPDKUceb4OLroz2YT1QsLjkWD6UNAhkyqM_8KnF6j8W_jnGD94YW_BKGykeVMCKYuGqxFTAdYTXg_ItmTX0StN9i1lYDOuFSz6wZ4IMGVwks7f8kjn3E4BgBbKGe8sCrmOZpzRQmWaUz4fBWNPTyqwbC5uPBhWlzQb56kVqNwDHnJ7Ss8eAMVy020sbsZ7E1cHSWAWfaj-jvyaF_HXHzDcIlSg_kp51DdgXC_Dyir5qYGloxtdeORrwfzA.SbVR9GMvusLnuOOtXcDvnw/__results___files/__results___95_1.png'
    st.image(image_url, caption='Important Features', use_column_width=True) 
