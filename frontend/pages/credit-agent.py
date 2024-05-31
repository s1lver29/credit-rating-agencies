import streamlit as st
from requests import get
import json
import re
from utils.utils import hide_streamlit_style, sidebar_remove

@st.cache_resource
def remove():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(sidebar_remove, unsafe_allow_html=True)


def _get_color(attr):
    # clip values to prevent CSS errors (Values should be from [-1,1])
    attr = max(-1, min(1, attr))
    if attr > 0:
        hue = 120
        sat = 75
        lig = 100 - int(50 * attr)
    else:
        hue = 0
        sat = 75
        lig = 100 - int(-40 * attr)
    return "hsl({}, {}%, {}%)".format(hue, sat, lig)


def app():
    st.title("Подробная информация")


    if "id" in st.query_params.keys():
        id_press_release = st.query_params["id"]

        response = get(f"http://127.0.0.1:8000/text_release/{id_press_release}")

        text_press_release, summary_release = json.loads(response.content)

        st.subheader(f"Категория: {summary_release['rating']}")

        text = ""
        s = re.compile(r"\(.*?\)")
        for word in text_press_release["text"].split(" "):
            if "[UNK]" in word:
                continue
            if len(s.findall(word)) == 0:
                continue
            color_ = re.sub(r"(\()|(\))", "", s.findall(word)[0][1:])
            color = _get_color(float(color_))
            word = s.sub("", word)
            if word in ".,»>":
                text = text[:len(text)-1]
            if word in "«<":
                text += f"""<span style="background-color: {color};line-height:1.75">{word}"""
                continue
            text += f"""<span style="background-color: {color};line-height:1.75">{word} """

        st.write(text, unsafe_allow_html=True)

remove()
app()
