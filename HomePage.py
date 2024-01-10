import common
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title=common.title, page_icon=":skull:", layout="wide")

st.write(f"""
# {common.title}
___
""")

common.sidebar()

col1, col2 = st.columns(2)




