from funciones import grafico_matplot
from funciones import grafico_seaborn
import streamlit as st
import pandas as pd




df = pd.read_csv('data.csv')
list_country = df['Country'].tolist()

country= st.selectbox("Select Country",list_country)


#print(mi_lista)

# st.table(df.head())
st.dataframe(df)

# country = 'Colombia'

grafico_matplot(country)
#grafico_seaborn(country)


