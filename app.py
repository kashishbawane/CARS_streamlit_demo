import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("CARS.csv")

st.title("Car Horsepower Visualization")

# Show available brands
brands = df['Make'].unique()
selected_brand = st.selectbox("Select a Car Brand:", brands)

# Filter data
s = df[df['Make'] == selected_brand]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
sb.barplot(x=s['Model'], y=s['Horsepower'], ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()

# Display chart
st.pyplot(fig)
