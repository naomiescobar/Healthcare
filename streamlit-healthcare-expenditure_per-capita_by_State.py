import streamlit as st
import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/naomiescobar/Healthcare/main/healthcare-expenditure_per-capita_by_State.csv"
data = pd.read_csv(url)

st.sidebar.title("Select States")
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
else:
    st.warning("Please select at least one state.")

    
'''Notes
The Centers for Medicare and Medicaid Services (CMS) Office of the Actuary produces Health Expenditures by State of Residence and Health Expenditures by State of Provider every five years. The State Health Expenditure Accounts are a subcomponent of the National Health Expenditure Accounts (NHEA), the official government estimates of health spending in the United States.  

Sources
Centers for Medicare & Medicaid Services, Office of the Actuary, National Health Statistics Group. [National Health Expenditure Data: Health Expenditures by State of Residence](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/NationalHealthExpendData/NationalHealthAccountsStateHealthAccountsResidence.html), August 2022.

Definitions
*Health Spending Per Capita* includes spending for all privately and publicly funded personal health care services and products (hospital care, physician services, nursing home care, prescription drugs, etc.) by state of residence (aggregate spending divided by population). Hospital spending is included and reflects the total net revenue (gross charges less contractual adjustments, bad debts, and charity care). Costs such as insurance program administration, research, and construction expenses are not included in this total.
'''
