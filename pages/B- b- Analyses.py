import common
from pathlib import Path
import pandas as pd
import streamlit as st

title = "Analyse"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()