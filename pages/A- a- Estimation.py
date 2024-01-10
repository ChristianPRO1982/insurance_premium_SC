import common
import streamlit as st

title = "Estimateur"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

st.write(
"""
Homme

Femme

age

BMI

Fumeur
""")