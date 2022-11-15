from operator import index
import streamlit as st
import plotly.express as px

import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

with st.sidebar: 
    st.image("favpng_future-ico.png")
    st.title("AutoNickML")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This is a simple project that shows how powerful open-source comunity has become", icon='🐍')