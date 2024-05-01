import streamlit as st
import pandas as pd
import plotly.express as px

# graph 1
url_graph1 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/streamlit_main.py/healthcare-expenditure%20per%20capita%20by%20State.csv"
data_graph1 = pd.read_csv(url_graph1)

st.sidebar.title("Select States")
selected_states = st.sidebar.multiselect("Choose states", data_graph1['State'].unique())

# menu to select states
filtered_data_graph1 = data_graph1[data_graph1['State'].isin(selected_states)]

# bar chart
if len(selected_states) > 0:
    st.title("Healthcare Expenditure per Capita Comparison")
    
    fig = px.bar(filtered_data_graph1, x='State', y='Health Spending per Capita', color='State', title='Healthcare Expenditure per Capita by State')
    fig.update_layout(xaxis_title='State', yaxis_title='Healthcare Expenditure per Capita')
    
    # show the chart
    st.plotly_chart(fig)

# graph 2
url_graph2 = "https://storage.googleapis.com/scsu-data-science/health-expenditure-2000-2020.csv"
data_graph2 = pd.read_csv(url_graph2)

st.sidebar.title("Health Expenditure per capita 2000-2020")
selected_countries = st.sidebar.multiselect("Choose countries", data_graph2['Country Name'].unique())

# menu to select countries
filtered_data_graph2 = data_graph2[data_graph2['Country Name'].isin(selected_countries)]

# line chart
if len(selected_countries) > 0:
    st.title("Health Expenditure Comparison")
    fig = px.line(filtered_data_graph2, x='Year', y='Health Expenditure (per capita)', color='Country Name')
    st.plotly_chart(fig)

# graph 3
url_graph3 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/us-healthcare-expenditure%20private%20vs.%20public%20(GDP).csv"
us_data = pd.read_csv(url_graph3)

st.sidebar.title("Health Expenditure GPD (Private vs. Public)")
option_private = st.sidebar.checkbox("US Health Expenditure, Private")
option_public = st.sidebar.checkbox("US Health Expenditure, Public")

# Filter data based on selected options
selected_data = []
if option_private:
    selected_data.append('US Health Expenditure, Private (US Census and WDI (2013))')
if option_public:
    selected_data.append('US Health Expenditure, Public (US Census and WDI (2013))')

if selected_data:
    st.subheader("Health Expenditure Comparison")
    melted_data_graph3 = us_data.melt(id_vars=['Year'], value_vars=selected_data, var_name='Data Type', value_name='Expenditure')
    fig = px.line(melted_data_graph3, x='Year', y='Expenditure', color='Data Type')
    st.plotly_chart(fig)
