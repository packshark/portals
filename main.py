import streamlit as st
import os
import pathlib

# Main content
st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

# Display login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button('Submit')

# Get the current path of the main file
current_path = pathlib.Path(__file__)

# Get the directory of the current path
current_dir = os.path.dirname(current_path)

# Change the destination URL to '/mount/src/portals/pages/cust.py'
new_path = os.path.join(current_dir, 'pages', 'cust.py')

if submit_button:
    if username == "phone" and password == "hellokitty":
        #url = "https://customerport.streamlit.app/"
        #st.markdown(f"[Right click to open in a new tab then close this]({{url}})")
        st.switch_page(new_path)
    elif username == "laptop" and password == "chamberofsecrets":
        st.switch_page("../pages/operations.py")
    elif username == "hehe" and password == "helloworld":
        st.switch_page(".pages/basicUser.py")
    else:
        st.error("Incorrect username or password")

