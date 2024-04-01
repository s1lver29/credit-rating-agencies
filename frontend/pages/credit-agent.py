import streamlit as st
from utils.db import get_press_release

if "id" in st.query_params.keys():
    id_press_release = st.query_params["id"]

    press_release = get_press_release(id_press_release)
    st.write(press_release[0])
    st.write(press_release[1])
