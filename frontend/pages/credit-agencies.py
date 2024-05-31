import streamlit as st
import pandas as pd
from requests import get
import json
from utils.utils import hide_streamlit_style, sidebar_remove

@st.cache_resource
def remove():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(sidebar_remove, unsafe_allow_html=True)

def apply_link(id: int):
    return f'<a target="_self" href="credit-agent?id={id}">Подробнее</a>'

def app():
    st.markdown(
        """
        <style>
            .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            width: 100%;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            }
            .styled-table thead tr {
                width: 100%;
                background-color: #009879;
                color: #ffffff;
                text-align: left;
            }
            .styled-table th,
            .styled-table td {
                padding: 12px 15px;
            }
            .styled-table tbody tr {
                border-bottom: 1px solid #dddddd;
            }
            .styled-table tbody tr:nth-of-type(even) {
                background-color: #f3f3f3;
            }
            .styled-table tbody tr:last-of-type {
                border-bottom: 2px solid #009879;
            }
            .styled-table tbody tr.active-row {
                font-weight: bold;
                color: #009879;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
    
    st.title("Сводка по анализу текстовых пресс-релизов")
    
    response = get(url="http://127.0.0.1:8000/cra-summaries")
    data = json.loads(response.content)
    
    table = pd.DataFrame(data=data)
    
    if not len(table) == 0:
        table["link"] = table["id"].apply(apply_link)
        table.drop(columns=["id"], inplace=True)
    
    table = table.rename(columns={
        "rating": "Категория",
        # "rating_details": "Рейтинг",
        "summary": "Пресс-релиз",
        "link": "Ссылка на анализ пресс-релиза"
    })
    
    st.write(table.to_html(escape=False, classes="styled-table", index=False, justify="left"), unsafe_allow_html=True)

remove()
app()