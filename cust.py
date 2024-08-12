import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title("Customer Portal")
st.markdown("Customer Portal")
st.sidebar.header("Customer Portal")
st.sidebar.header("Operations Portal")

# table Rithik shared -- though we might not need this once we have the Power BI table and can do everything through there
data = pd.read_csv("https://github.com/packshark/portals/blob/main/fake_dns_log.csv")
st.dataframe(table, height=750)

# Power BI table
# do we want to upload and reflect anything?
components.iframe("https://app.powerbi.com/reportEmbed?reportId=c2d0d27d-4aab-4cb8-94ab-f793dade383c&autoAuth=true&ctid=e741d71c-c6b6-47b0-803c-0f3b32b07556", height =600, width = 800)
# <iframe title="nathaniel's non-user error report" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=c2d0d27d-4aab-4cb8-94ab-f793dade383c&autoAuth=true&ctid=e741d71c-c6b6-47b0-803c-0f3b32b07556" frameborder="0" allowFullScreen="true"></iframe>
