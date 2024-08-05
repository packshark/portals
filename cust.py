import streamlit as st
import pandas as pd

st.title("Customer Portal")

# sample table until we have the data
table = pd.DataFrame({"User": ["Stephanie","Jeremy","Nathaniel","Christiana","Rithik"],
                      "Device": ["Mobile","Desktop","Tablet","Watch","TV"],
                      "Blocked_Domains": ["https://blahblah.com","hahahahah.com","https://fkshdfkjsfhks.com","https://fafsa.gov","bing.com"],
                      "Count":[20,5,2,4,5]})
st.table(table)