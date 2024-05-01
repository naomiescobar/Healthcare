import streamlit as st
import pandas as pd
import altair as alt

# graph 1
url = "https://raw.githubusercontent.com/naomiescobar/Healthcare/streamlit_main.py/healthcare-expenditure%20per%20capita%20by%20State.csv"
data = pd.read_csv(url)

st.sidebar.title("Health Expenditure per capita (by State)")
selected_states = st.sidebar.multiselect("Choose states", data['State'].unique())

# menu to select states
filtered_data = data[data['State'].isin(selected_states)]

# bar chart
if len(selected_states) > 0:
    st.title("Healthcare Expenditure per Capita Comparison")

    fig = px.bar(filtered_data, x='State', y='Health Spending per Capita', color='State', title='Healthcare Expenditure per Capita by State')
    
    # update
    fig.update_layout(xaxis_title='State', yaxis_title='Healthcare Expenditure per Capita')

    # show the chart
    st.plotly_chart(fig)

    

# graph 2
url = "https://storage.googleapis.com/scsu-data-science/health-expenditure-2000-2020.csv"
data = pd.read_csv(url)

st.sidebar.title("Health Expenditure per capita 2000-2020")
selected_countries = st.sidebar.multiselect("Choose countries", data['Country Name'].unique())

# menu to select countries
filtered_data = data[data['Country Name'].isin(selected_countries)]

# columns representing the years
year_columns = [str(year) for year in range(2000, 2024)]

# melt the data to have 'Year' as a variable
melted_data = filtered_data.melt(id_vars=['Country Name'], value_vars=year_columns, var_name='Year', value_name='Health Expenditure (per capita)')

# Convert 'Year' to int
melted_data['Year'] = melted_data['Year'].astype(int)

# line chart
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




# graph 3
url = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/us-healthcare-expenditure%20private%20vs.%20public%20(GDP).csv"
us_data = pd.read_csv(url)

st.sidebar.title("Health Expenditure GPD (Private vs. Public)")
option_private = st.sidebar.checkbox("US Health Expenditure, Private")
option_public = st.sidebar.checkbox("US Health Expenditure, Public")

# line chart
st.title("Health Expenditure Comparison")

# Filter data based on selected options
selected_data = []
if option_private:
    selected_data.append('US Health Expenditure, Private (US Census and WDI (2013))')
if option_public:
    selected_data.append('US Health Expenditure, Public (US Census and WDI (2013))')

if selected_data:
    st.subheader("Health Expenditure Comparison")
    melted_data = us_data.melt(id_vars=['Year'], value_vars=selected_data, var_name='Data Type', value_name='Expenditure')
    chart = alt.Chart(melted_data).mark_line().encode(
        x='Year:O',
        y='Expenditure',
        color='Data Type'
    ).properties(
        width=800,
        height=500
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Please select at least one data option.")
