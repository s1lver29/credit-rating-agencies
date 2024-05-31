import streamlit as st
# from st_pages import show_pages_from_config, add_page_title
from utils.utils import hide_streamlit_style, sidebar_remove


@st.cache_data
def main():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(sidebar_remove, unsafe_allow_html=True)
    # show_pages_from_config()
    # add_page_title()

    
    

if __name__ == "__main__":
    main()