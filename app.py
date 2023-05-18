#app.py
#Author: Natalia Kuzminykh

#Importing libraries
import random
import streamlit as st

#Importing functions from other files
from config import set_page_config, footer
from utils import *

# Set the page configuration
set_page_config()

#Initializing the session state
def init_session_state():
    if 'level' not in st.session_state:
        st.session_state['level'] = 0
        st.session_state['tasks'] = []

##############################################################################################################
#Main code

#Creating the app interface
st.markdown('<h2 style="text-align: center;">🚀 School 42 Exam Simulator: Rank 02</h2>', unsafe_allow_html=True)
st.markdown('<h4 style="text-align: center;font-weight: normal">This exam has 4 questions in total. A random question is picked from each level below.</h4>', unsafe_allow_html=True)   

#Initializing the session state
init_session_state()
 
#Creating a progress bar
progress_bar = st.progress(min(st.session_state['level'] / 4, 1))

select_level()

if st.session_state['level'] == 0:
    start_exam(levels[1], progress_bar)

display_exam() 
 
if 0 < st.session_state['level'] < 4:
    next_level(levels[st.session_state['level'] + 1], progress_bar)

elif st.session_state['level'] == 4:
    finish_exam(progress_bar)

#We did it! The exam is over!
if st.session_state['level'] == 5:
    st.markdown('<h2 style="text-align: center;"><br> Congratulations! <br> You successfully passed the exam!</h2>', unsafe_allow_html=True)
    st.balloons()  # Celebrate with balloons.
    start_over()

# Display the footer
footer()