# a user that does not have access to see everything
import streamlit as st
import pandas as pd
from io import StringIO

st.title("Uploading Files")
st.subheader("You have reached this page due to your current access permissions")
st.markdown("---")

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# Can be used wherever a "file-like" object is accepted:
dataframe = pd.read_csv(uploaded_file)
st.write(dataframe)

# later want to pass this to powerBI
