import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title("Customer Portal")
st.markdown("Customer Portal")
st.sidebar.header("Customer Portal")
st.sidebar.header("Operations Portal")

# add filters
# sample table until we have the data
table = pd.DataFrame({"User": ["Stephanie","Jeremy","Nathaniel","Christiana","Rithik"],
                      "Device": ["Mobile","Desktop","Tablet","Watch","TV"],
                      "Blocked_Domains": ["https://blahblah.com","hahahahah.com","https://fkshdfkjsfhks.com","https://fafsa.gov","bing.com"],
                      "Count":[20,5,2,4,5]})
st.table(table)

# Power BI table
# do we want to upload and reflect anything?
components.iframe("https://app.powerbi.com/reportEmbed?reportId=c2d0d27d-4aab-4cb8-94ab-f793dade383c&autoAuth=true&ctid=e741d71c-c6b6-47b0-803c-0f3b32b07556", height =750, width = 1140)
# <iframe title="nathaniel's non-user error report" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=c2d0d27d-4aab-4cb8-94ab-f793dade383c&autoAuth=true&ctid=e741d71c-c6b6-47b0-803c-0f3b32b07556" frameborder="0" allowFullScreen="true"></iframe>
