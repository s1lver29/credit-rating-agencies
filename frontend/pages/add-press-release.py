import streamlit as st
from utils.db import create_new_entry

text = st.text_area("Текст пресс-релиза", height=400, label_visibility="hidden")

button = st.button("Отправить")

if button:
    create_new_entry(text=text)
    st.markdown('<meta http-equiv="refresh" content="0;URL=/credit-agencies">', unsafe_allow_html=True)

