import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Datasets/CARS.csv")

# Streamlit title
st.title("Car Horsepower Visualization")

# Show sample data
st.write("### Preview of Data")
st.write(df.head(5))

# Dropdown for selecting brand
brands = df['Make'].unique()
brand = st.selectbox("Select a Car Brand", brands)

# Filter data by brand
s = df[df['Make'] == brand]

# Plot with seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sb.barplot(x="Model", y="Horsepower", data=s, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
