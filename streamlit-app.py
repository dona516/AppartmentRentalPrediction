import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # dataviz
import seaborn as sns
import streamlit as st

st.title("Rental Analysis Visualisations")
url = "https://raw.githubusercontent.com/Jerin-T/streamlit/main/dataset.csv"
df = pd.read_csv(url, index_col=0)

numerical_columns = df.select_dtypes(include='number')

fig = plt.figure(figsize=(20, 15))

num_plots = len(numerical_columns.columns)  # Total number of plots
num_rows = (num_plots // 5) + 1  # Calculate the number of rows needed

for i, col in enumerate(numerical_columns.columns):
    plt.subplot(num_rows, 5, i+1)  # Adjusting subplot position
    sns.boxplot(y=numerical_columns[col], showfliers=True)
    plt.title(col)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
st.pyplot(fig)

numerical_columns = df.select_dtypes(include='number')

fig1 = plt.figure(figsize=(20, 15))

num_plots = len(numerical_columns.columns)  # Total number of plots
num_rows = (num_plots // 5) + 1  # Calculate the number of rows needed

for i, col in enumerate(numerical_columns.columns):
    plt.subplot(num_rows, 5, i+1)  # Adjusting subplot position
    sns.boxplot(y=numerical_columns[col], showfliers=True)
    plt.title(col)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
st.pyplot(fig1)

# Set seaborn style
sns.set_style("whitegrid")

# 2. Box plot for comparing livingSpace across typeOfFlat
fig3 = plt.figure(figsize=(15, 9))
sns.boxplot(x='typeOfFlat', y='livingSpace', data=df)
plt.title('Living Space by Type of Flat')
plt.show()
st.pyplot(fig3)

# 3. Scatter plot between livingSpace and baseRent
fig4 = plt.figure(figsize=(10, 6))
sns.scatterplot(x='livingSpace', y='baseRent', data=df)
plt.title('Base Rent vs. Living Space')
plt.show()
st.pyplot(fig4)

fig8 = plt.figure(figsize=(12, 6))
sns.countplot(x='typeOfFlat', data=df)
plt.title('Count Plot of Type of Flat')
plt.show()
st.pyplot(fig8)

fig9 = plt.figure(figsize=(14, 8))
sns.barplot(x='regio1', y='totalRent', data=df, ci=None, estimator=np.mean)
plt.title('Average Total Rent by Region')
plt.show()
st.pyplot(fig9)

fig10 = plt.figure(figsize=(12, 6))
sns.barplot(x='typeOfFlat', y='livingSpace', data=df, ci=None, estimator=np.mean)
plt.title('Average Living Space by Type of Flat')
plt.show()
st.pyplot(fig10)

f3 = plt.figure(figsize=(12, 6))
sns.scatterplot(x='livingSpace', y='totalRent', size='noRooms', hue='typeOfFlat', data=df, alpha=0.6)
plt.title('Bubble Chart of Total Rent vs. Living Space (bubble size: noRooms, hue: typeOfFlat)')
plt.show()
st.pyplot(f3)

f5 = plt.figure(figsize=(12, 6))
sns.stripplot(x='typeOfFlat', y='totalRent', data=df, jitter=True)
plt.title('Strip Plot of Total Rent by Type of Flat')
plt.show()
st.pyplot(f5)