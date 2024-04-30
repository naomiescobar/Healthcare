import streamlit as st
import pandas as pd
import altair as alt

# Load the data
url = "https://storage.googleapis.com/scsu-data-science/health-expenditure-2000-2020.csv"
data = pd.read_csv(url)

# Sidebar
st.sidebar.title("Select Countries")
selected_countries = st.sidebar.multiselect("Choose countries", data['Country Name'].unique())

# Filter data based on selected countries
filtered_data = data[data['Country Name'].isin(selected_countries)]

# Get the columns representing years
year_columns = [str(year) for year in range(2000, 2024)]

# Melt the data to have 'Year' as a variable
melted_data = filtered_data.melt(id_vars=['Country Name'], value_vars=year_columns, var_name='Year', value_name='Health Expenditure (per capita)')

# Convert 'Year' to int
melted_data['Year'] = melted_data['Year'].astype(int)

# Line chart
if len(selected_countries) > 0:
    st.title("Health Expenditure Comparison")
    chart = alt.Chart(melted_data).mark_line().encode(
        x='Year:O',
        y='Health Expenditure (per capita)',
        color='Country Name'
    ).properties(
        width=800,
        height=500
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Please select at least one country.")
