import streamlit as st
import pandas as pd
import altair as alt

# Load data for graph 1
url_graph1 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/streamlit_main.py/healthcare-expenditure%20per%20capita%20by%20State.csv"
data_graph1 = pd.read_csv(url_graph1)

# Load data for graph 2
url_graph2 = "https://storage.googleapis.com/scsu-data-science/health-expenditure-2000-2020.csv"
data_graph2 = pd.read_csv(url_graph2)

# Load data for graph 3
url_graph3 = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/us-healthcare-expenditure%20private%20vs.%20public%20(GDP).csv"
us_data = pd.read_csv(url_graph3)

# Sidebar navigation
page = st.sidebar.radio("Select Page", ["Graph 1", "Graph 2", "Graph 3"])

# Display selected graph
if page == "Graph 1":
    st.title("Graph 1: Healthcare Expenditure per Capita Comparison")
    st.write("You can choose any state and compare the Health Expenditures. This indicator calculates the average expenditure on health per person in comparable currency including the purchasing power of national currencies. It contributes to understanding the health expenditure relative to the population size facilitating national comparison.")
    
    selected_states = st.multiselect("Choose states", data_graph1['State'].unique())

    # menu to select states
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

elif page == "Graph 2":
    st.title("Graph 2: Health Expenditure Comparison")
    st.write("Health expenditure per capita is the amount that each country spends on health, for both individual and collective services, and how this changes over time can be the result of a wide array of social and economic factors, as well as the financing and organisational structures of a country's health system. You can choose any country and compare the Health Expenditures and compare them in the graph. Health expenditure data reveal strengths, weaknesses, and areas needing investment like health facilities, information systems, and human resources.")
    
    selected_countries = st.multiselect("Choose countries", data_graph2['Country Name'].unique())

    # menu to select countries
    filtered_data_graph2 = data_graph2[data_graph2['Country Name'].isin(selected_countries)]

    # columns representing the years
    year_columns = [str(year) for year in range(2000, 2024)]

    # melt the data to have 'Year' as a variable
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

elif page == "Graph 3":
    st.title("Graph 3: Health Expenditure GPD (Private vs. Public)")
    st.write("This indicator is defined as the level of total expenditure on health expressed as a percentage of GDP, where GDP is the value of all final goods and services produced within a nation in a given year.")
    st.write("Government insurance programs, such as Medicare and Medicaid, made up 45 percent, or $1.9 trillion, of national healthcare spending. Private insurance programs, including employer-provided health insurance as well as plans purchased through the Affordable Care Act, accounted for 30 percent, or about $1.3 trillion.")
    st.write("More than 17 percent of the U.S. Gross Domestic Product is spent on health care—in many cases, for conditions that could be prevented or better managed with public health interventions. Yet only 3 percent of the government's health budget is spent on public health measures.")

    option_private = st.checkbox("US Health Expenditure, Private")
    option_public = st.checkbox("US Health Expenditure, Public")

    # Filter data based on selected options
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
