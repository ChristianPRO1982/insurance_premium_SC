import common
import streamlit as st
import sklearn_pkg

st.set_page_config(page_title=common.title, page_icon="#", layout="wide")

st.write(f"""
# {common.title}
___
""")

common.sidebar()
if st.sidebar.button("Entrainement"):
    st.success(sklearn_pkg.train())
    common.train_done = True
    st.sidebar.empty()

col1, col2 = st.columns(2)




