import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Car Horsepower Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Load Dataset ----------
@st.cache_data
def load_data():
    df = pd.read_csv("CARS.csv")
    return df

df = load_data()

# ---------- Title & Description ----------
st.title("🚗 Car Horsepower Analyzer")
st.markdown("""
### Explore and Compare Car Horsepower
Select a brand to visualize horsepower trends across different models, 
filter by year or fuel type, and discover top-performing vehicles.
""")

# ---------- Sidebar Filters ----------
st.sidebar.header("🔍 Filter Options")

brands = sorted(df['Make'].unique())
selected_brand = st.sidebar.selectbox("Select Brand:", brands)

# Optional Filters
if 'Year' in df.columns:
    years = sorted(df['Year'].unique())
    selected_year = st.sidebar.multiselect("Filter by Year:", years, default=years)
else:
    selected_year = None

if 'Fuel_Type' in df.columns:
    fuel_types = sorted(df['Fuel_Type'].unique())
    selected_fuel = st.sidebar.multiselect("Select Fuel Type:", fuel_types, default=fuel_types)
else:
    selected_fuel = None

chart_type = st.sidebar.radio("Chart Type:", ["Bar Chart", "Line Chart", "Scatter Plot", "Box Plot", "Pie Chart"])
show_data = st.sidebar.checkbox("Show Data Table")
download_button = st.sidebar.button("⬇️ Download Filtered Data")

# ---------- Filter Data ----------
filtered_df = df[df['Make'] == selected_brand]
if selected_year:
    filtered_df = filtered_df[filtered_df['Year'].isin(selected_year)]
if selected_fuel:
    filtered_df = filtered_df[filtered_df['Fuel_Type'].isin(selected_fuel)]

# ---------- Key Insights ----------
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Models", len(filtered_df))
col2.metric("Average Horsepower", f"{filtered_df['Horsepower'].mean():.1f}")
col3.metric("Max Horsepower", f"{filtered_df['Horsepower'].max():.0f}")
col4.metric("Min Horsepower", f"{filtered_df['Horsepower'].min():.0f}")

# ---------- Visualization ----------
st.markdown("---")
st.subheader(f"📊 Horsepower Visualization for {selected_brand}")

if not filtered_df.empty:
    if chart_type == "Bar Chart":
        fig = px.bar(filtered_df, x="Model", y="Horsepower", color="Horsepower",
                     color_continuous_scale="viridis", title=f"{selected_brand} - Horsepower by Model")
    elif chart_type == "Line Chart":
        fig = px.line(filtered_df, x="Model", y="Horsepower", markers=True, color_discrete_sequence=["orange"])
    elif chart_type == "Scatter Plot":
        fig = px.scatter(filtered_df, x="Model", y="Horsepower", color="Horsepower",
                         size="Horsepower", hover_data=["Model"])
    elif chart_type == "Box Plot":
        fig = px.box(filtered_df, x="Model", y="Horsepower", color="Model")
    elif chart_type == "Pie Chart":
        fig = px.pie(filtered_df, names="Model", values="Horsepower",
                     title=f"{selected_brand} - Horsepower Distribution")

    fig.update_layout(xaxis_title="Car Model", yaxis_title="Horsepower", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ No data available for the selected filters.")

# ---------- Show Data Table ----------
if show_data:
    st.markdown("### 📋 Filtered Data Table")
    st.dataframe(filtered_df)

# ---------- Download CSV ----------
if download_button:
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"{selected_brand}_Horsepower_Data.csv",
        mime="text/csv"
    )

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Developed with ❤️ using Streamlit | Data Source: Car Dataset</p>",
    unsafe_allow_html=True
)

st.pyplot(fig)
# --- Visualization ---
st.markdown("---")
st.subheader(f"📊 Horsepower Visualization for {selected_brand}")

if not filtered_df.empty:
    if chart_type == "Bar Chart":
        fig = px.bar(filtered_df, x="Model", y="Horsepower", color="Horsepower",
                     color_continuous_scale="viridis", title=f"{selected_brand} - Horsepower by Model")
    elif chart_type == "Line Chart":
        fig = px.line(filtered_df, x="Model", y="Horsepower", markers=True, color_discrete_sequence=["orange"])
    elif chart_type == "Scatter Plot":
        fig = px.scatter(filtered_df, x="Model", y="Horsepower", color="Horsepower",
                         size="Horsepower", hover_data=["Model"])
    elif chart_type == "Box Plot":
        fig = px.box(filtered_df, x="Model", y="Horsepower", color="Model")
    elif chart_type == "Pie Chart":
        fig = px.pie(filtered_df, names="Model", values="Horsepower",
                     title=f"{selected_brand} - Horsepower Distribution")

    # ✅ Use this for Plotly
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ No data available for the selected filters.")

