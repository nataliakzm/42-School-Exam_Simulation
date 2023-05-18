# config.py
import streamlit as st

# Set the page configuration
def set_page_config():
    st.set_page_config(
        page_title="School 42 Exam Simulator",
        page_icon="🚀",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'Report a bug': "https://github.com/nataliakzm/42-School-Exam_Simulation",
            'About': "#### The School 42 Exam Simulator is the perfect tool for anyone getting ready for their first exam in School 42's Cursus."
        }
    )

# Display the footer
def footer():
    st.markdown("""
        <div style="position: fixed; bottom: 10px; right: 10px; text-align: right;">
            Made by <a href="https://github.com/nataliakzm" target="_blank">@nataliakzm</a> 👩🏽‍💻
            <br>
            <br>
            <br>        
        </div>
        """, unsafe_allow_html=True)