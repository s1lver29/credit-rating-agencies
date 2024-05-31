import streamlit as st
from requests import post
import json
from copy import copy
from utils.utils import hide_streamlit_style, sidebar_remove

@st.cache_resource
def remove():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(sidebar_remove, unsafe_allow_html=True)

st.markdown("""
            <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            [data-testid="baseButton-header"] {
                display: none
            }
            </style>
            """, unsafe_allow_html=True)


def clear_text():
    st.session_state.text = copy(st.session_state.press_release_text)
    st.session_state.press_release_text = ""

def app():
    st.title("Анализ нового пресс-релиза")

    st.text_area(label="Текст пресс-релиза", height=400, label_visibility="hidden", key="press_release_text")
    
    button = st.button("Отправить", on_click=clear_text)
    
    
    if button:
        inputs = {
            "text": st.session_state.text
        }
        post("http://127.0.0.1:8000/predict_model", data = json.dumps(inputs))
    
        st.toast("Принято в работу  \n\n\nСводка по пресс-релизу будет [тут](./credit-agencies)", icon="🤖")
    # st.markdown('<meta http-equiv="refresh" content="0;URL=/credit-agencies">', unsafe_allow_html=True)

remove()
app()

