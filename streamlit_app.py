import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="Customer Portal")
st.title("Customer Portal")
st.write(
    """
    This is to view the users and devices on the network. The user can filter and view some statistics.
    """
)

# Create a random Pandas dataframe
if "df" not in st.session_state:

    # Set seed for reproducibility.
    np.random.seed(42)

    start_mac_num = 100000000000
    end_mac_num = 100000000000+100
    # Generate the dataframe with 100 rows/logs. This will be refined later
    data = {
        "MAC":[for i in range(start_mac_num, end_mac_num)],
        "ID": [f"TICKET-{i}" for i in range(1100, 1000, -1)],
        "User": [random.choice(['Ari', 'Taylor', 'Justin', 'Rocky']) for _ in range(start_num, end_num)],
        "Device": [random.choice(['Desktop', 'Tablet', 'Mobile', 'TV']) for _ in range(start_num, end_num)],
        "Count": [random.randint(1, 10) for _ in range(start_num, end_num)],
        "Date": [
            datetime.date(2023, 6, 1) + datetime.timedelta(days=random.randint(0, 182))
            for _ in range(100)
        ],
    }
    df = pd.DataFrame(data)

    # Save the dataframe in session state (a dictionary-like object that persists across
    # page runs). This ensures our data is persisted when the app updates.
    st.session_state.df = df

# Show some metrics and charts about the user -- when they have the power bi




