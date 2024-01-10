import common
from pathlib import Path
import pandas as pd
import streamlit as st

title = "Estimateur"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

@st.cache_data
def load_data():
   bikes_data_path = Path() / 'data_cleaned_cheated.csv'
   data = pd.read_csv(bikes_data_path)
   return data

df = load_data()
st.write(df)