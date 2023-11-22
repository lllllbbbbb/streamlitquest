import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
#scaling of dataframe
from sklearn import preprocessing

x = df.select_dtypes(np.number).values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
df_scaled = pd.DataFrame(x_scaled)

choice = st.radio("Choisissez une région", [' US.', ' Europe.', ' Japan.'])

rr = px.scatter(df.loc[df.continent == choice],x='hp',y='time-to-60')
st.plotly_chart(rr)
