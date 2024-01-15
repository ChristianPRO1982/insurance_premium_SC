import common
import streamlit as st

title = "Une petite histoire"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
common.sidebar(option=False)

st.success("### On n'est pas là pour déconner")