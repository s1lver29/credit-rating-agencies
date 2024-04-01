import streamlit as st
import pandas as pd
from utils.db import get_list_press_releases

def apply_link(id: int):
    return f'<a target="_self" href="credit-agent?id={id}">Подробнее</a>'

data = get_list_press_releases()

table = pd.DataFrame(data={
    "ids": data["ids"],
    "rating": data["ratings"],
    "summary": data["summaries"],
})

table["link"] = table["ids"].apply(apply_link)
table.drop(columns=["ids"], inplace=True)


st.write(table.to_html(escape=False), unsafe_allow_html=True)