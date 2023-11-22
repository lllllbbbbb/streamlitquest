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


#plotting of distribution
fig1, ax1 = plt.subplots()
ax1 = sns.heatmap(df.select_dtypes(np.number).corr(), annot=True)
st.pyplot(fig1)

#fig2, ax2 = plt.subplots()
fig2, axes = plt.subplots(nrows=2,ncols=4,figsize=(10,5))

for i, column in enumerate(df.select_dtypes(np.number).columns):
    sns.boxplot(df, y=column, ax=axes[i//4][i%4])
axes[1,3].set_axis_off()
plt.tight_layout()

st.pyplot(fig2)
