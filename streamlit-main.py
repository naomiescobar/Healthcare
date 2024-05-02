import streamlit as st
import pandas as pd
import altair as alt

# graph 1
url_graph1 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/streamlit_main.py/healthcare-expenditure%20per%20capita%20by%20State.csv"
data_graph1 = pd.read_csv(url_graph1)

'''This indicator calculates the average expenditure on health per person in comparable currency including the purchasing power of national currencies. It contributes to understand the health expenditure relative to the population size facilitating national comparison.
'''


# graph 2
url_graph2 = "https://storage.googleapis.com/scsu-data-science/health-expenditure-2000-2020.csv"
data_graph2 = pd.read_csv(url_graph2)

''''''


# graph 3
url_graph3 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/us-healthcare-expenditure%20private%20vs.%20public%20(GDP).csv"
us_data = pd.read_csv(url_graph3)

# sidebar 
page = st.sidebar.radio("Select Page", ["Healthcare Expenditure per Capita Comparison", "Health Expenditure Comparison", "Health Expenditure GPD (Private vs. Public"])

if page == "Healthcare Expenditure per Capita Comparison":
    st.title("Graph 1: Healthcare Expenditure per Capita Comparison")
    
    selected_states = st.multiselect("Choose states", data_graph1['State'].unique())

    # states menu
    filtered_data_graph1 = data_graph1[data_graph1['State'].isin(selected_states)]

    # bar chart
    if len(selected_states) > 0:
        fig = alt.Chart(filtered_data_graph1).mark_bar().encode(
            x='State',
            y='Health Spending per Capita',
            color='State'
        ).properties(
            width=800,
            height=500
        )
        # show the chart
        st.altair_chart(fig, use_container_width=True)
    else:
        st.warning("Please select at least one state.")

elif page == "Health Expenditure Comparison":
    st.title("Graph 2: Health Expenditure Comparison")
    
    selected_countries = st.multiselect("Choose countries", data_graph2['Country Name'].unique())

    # countries menu
    filtered_data_graph2 = data_graph2[data_graph2['Country Name'].isin(selected_countries)]

    # columns with years
    year_columns = [str(year) for year in range(2000, 2024)]
    melted_data_graph2 = filtered_data_graph2.melt(id_vars=['Country Name'], value_vars=year_columns, var_name='Year', value_name='Health Expenditure (per capita)')

    # Convert 'Year' to int
    melted_data_graph2['Year'] = melted_data_graph2['Year'].astype(int)

    # line chart
    if len(selected_countries) > 0:
        chart = alt.Chart(melted_data_graph2).mark_line().encode(
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

elif page == "Health Expenditure GPD (Private vs. Public":
    st.title("Graph 3: Health Expenditure GPD (Private vs. Public)")

    option_private = st.checkbox("US Health Expenditure, Private")
    option_public = st.checkbox("US Health Expenditure, Public")

    # filter the data based on selected options
    selected_data = []
    if option_private:
        selected_data.append('US Health Expenditure, Private (US Census and WDI (2013))')
    if option_public:
        selected_data.append('US Health Expenditure, Public (US Census and WDI (2013))')

    if selected_data:
        melted_data_graph3 = us_data.melt(id_vars=['Year'], value_vars=selected_data, var_name='Data Type', value_name='Expenditure')
        chart = alt.Chart(melted_data_graph3).mark_line().encode(
            x='Year:O',
            y='Expenditure',
            color='Data Type'
        ).properties(
            width=800,
            height=500
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    else:
        st.warning("Please select at least one option.")
