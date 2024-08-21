import streamlit as st
import os

# Main content
st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

# Display login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button('Submit')

if submit_button:
    if username == "phone" and password == "hellokitty":
        url = "https://customerport.streamlit.app/"
        st.markdown(f"[Right click to open in a new tab then close this]({{url}})")
    elif username == "laptop" and password == "chamberofsecrets":
        st.switch_page("./pages/operations.py")
    elif username == "hehe" and password == "helloworld":
        st.switch_page(".pages/basicUser.py")
    else:
        st.error("Incorrect username or password")
