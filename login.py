import streamlit as st
from navigation import make_sidebar
import sys

# Ensure session state is initialized
# if "logged_in" not in st.session_state:
    # st.session_state.logged_in = False

# Sidebar for navigation
# make_sidebar()

# Main content
st.title("Welcome to the Packing Portal")
st.write("Please log in to continue")

# Display login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button('Submit')

if submit_button:
    form_submitted = True
else:
    form_submitted = False
if form_submitted:
    if username == "phone" and password == "hellokitty":
        # st.session_state.logged_in = True
        #st.success("Logged in successfully!")
        # st.switch_page("workingcopy.py") #st.switch_page should work with updating the session state
        st.session_state['page'] = 'workingcopy.py'
        st.experimental_rerun()  # Reload the page to reflect the login state
    elif username == "laptop" and password == "chamberofsecrets":
        # st.session_state.logged_in = True
        st.success("Logged in successfully!")
        #st.experimental_rerun()  # Reload the page to reflect the login state
        st.switch_page("operations.py")
    elif username == "hehe" and password == "helloworld":
        # st.session_state.logged_in = True
        st.success("Logged in successfully!")
        #st.experimental_rerun()  # Reload the page to reflect the login state
        st.switch_page("basicUser.py")
    else:
        st.error("Incorrect username or password")
