import streamlit as st
import pandas as pd
import altair as alt

url = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/us-healthcare-expenditure%20private%20vs.%20public%20(GDP).csv"
us_data = pd.read_csv(url)

st.sidebar.title("Select Data")
data_option = st.sidebar.selectbox(
    "Choose data to compare",
    ['US Health Expenditure, Private', 'US Health Expenditure, Public']
)

# line chart
st.title("Health Expenditure Comparison")

if data_option == 'US Health Expenditure, Private':
    st.subheader("US Health Expenditure, Private (US Census and WDI (2013))")
    chart = alt.Chart(us_data).mark_line().encode(
        x='Year:O',
        y='US Health Expenditure, Private (US Census and WDI (2013))'
    ).properties(
        width=800,
        height=500
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

elif data_option == 'US Health Expenditure, Public':
    st.subheader("US Health Expenditure, Public (US Census and WDI (2013))")
    chart = alt.Chart(us_data).mark_line().encode(
        x='Year:O',
        y='US Health Expenditure, Public (US Census and WDI (2013))'
    ).properties(
        width=800,
        height=500
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("Please select a data option.")
