#Author: Natalia Kuzminykh
#Importing libraries
import streamlit as st
import random
import glob
import os

#Loading tasks from the tasks folder and displaying them in the app 
#   in a random order according to the level
def load_task(task_name):
    with open(f'tasks/{task_name}.txt', 'r') as f:
        content = f.read()
    parts = content.split('---')
    
    #Expected files and allowed functions
    expected_files, allowed_functions = parts[0].split('\n')[:2]
    expected_files = expected_files.split(':')[-1].strip()
    allowed_functions = allowed_functions.split(':')[-1].strip()
    
    #Task description
    description = parts[1].split(':', 1)[-1].strip()

    #Here, we place the Example part into a code block
    if 'Examples:' in description:
        desc_parts = description.split('Examples:')
        description = desc_parts[0] + 'Examples:\n```\n' + desc_parts[1].strip() + '\n```'
    return expected_files, allowed_functions, description

#Creating a list of tasks for each level
level_1 = [
    'first_word',
    'fizzbuzz',
    'ft_strcpy',
    'ft_strlen',
    'ft_swap',
    'ft_putstr',
    'repeat_alpha',
    'rev_print',
    'rot_13',
    'rotone',
    'search_and_replace',
    'ulstr'
]

level_2 = [
    'alpha_mirror',
    'camel_to_snake',
    'do_op',
    'ft_atoi',
    'ft_strcmp',
    'ft_strcspn',
    'ft_strdup',
    'ft_strpbrk',
    'ft_strrev',
    'ft_strspn',
    'inter',
    'is_power_of_2',
    'last_word',
    'max',
    'print_bits',
    'reverse_bits',
    'snake_to_camel',
    'swap_bits',
    'union',
    'wdmatch'
]

level_3 = [
    'add_prime_sum',
    'epur_str',
    'expand_str',
    'ft_atoi_base',
    'ft_list_size',
    'ft_range',
    'ft_rrange',
    'hidenp',
    'lcm',
    'paramsum',
    'pgcd',
    'print_hex',
    'rstr_capitalizer',
    'str_capitalizer',
    'tab_mult'
]

level_4 = [
    'flood_fill',
    'fprime',
    'ft_itoa',
    'ft_list_foreach',
    'ft_list_remove_if',
    'ft_split',
    'rev_wstr',
    'rostring',
    'sort_int_tab',
    'sort_list'
]


#Creating the app interface
st.markdown('<h2 style="text-align: center;">🚀 School 42 Exam Simulator: Rank 02</h2>', unsafe_allow_html=True)
st.markdown('<h4 style="text-align: center;font-weight: normal">This exam has 4 questions in total. A random question is picked from each level below.</h4>', unsafe_allow_html=True)   

#Initializing the session state
if 'level' not in st.session_state:
    st.session_state['level'] = 0
    st.session_state['tasks'] = []
    
#Creating a progress bar
progress_bar = st.progress(min(st.session_state['level'] / 4, 1))

#Creating a button to start the exam
if st.session_state['level'] == 0:
    if st.button('Start Exam'):
        st.session_state['level'] += 1
        task_name = random.choice(eval(f'level_{st.session_state["level"]}'))
        st.session_state['tasks'].append(task_name)
        progress_bar.progress(min(st.session_state['level'] / 4, 1))

for i in range(1, st.session_state['level'] + 1):
    if i <= 4:
        st.subheader(f'Level {i}')
        task_name = st.session_state['tasks'][i - 1]
        expected_files, allowed_functions, description = load_task(task_name)
        st.markdown(f'**Task:** {task_name}\n', unsafe_allow_html=True)
        st.markdown(f'**Expected files:** {expected_files}\n', unsafe_allow_html=True)
        st.markdown(f'**Allowed functions:** {allowed_functions}\n', unsafe_allow_html=True) 
        st.markdown(f'**Description:**\n{description}\n', unsafe_allow_html=True)
        
#Creating a button to move to the next level
if st.session_state['level'] > 0 and st.session_state['level'] < 4:
    if st.button(f'Next Level (Level {st.session_state["level"] + 1})'):
        st.session_state['level'] += 1
        task_name = random.choice(eval(f'level_{st.session_state["level"]}'))
        st.session_state['tasks'].append(task_name)
        progress_bar.progress(min(st.session_state['level'] / 4, 1))
        st.experimental_rerun()

elif st.session_state['level'] == 4:
    if st.button('Finish Exam'):
        st.session_state['level'] += 1
        progress_bar.progress(min(st.session_state['level'] / 4, 1))
        st.experimental_rerun()

#We did it! The exam is over!
if st.session_state['level'] == 5:
    st.subheader('Congratulations! You have completed the exam.')
    if st.button('Start Over'):
        st.session_state['level'] = 0
        st.session_state['tasks'] = []
        st.experimental_rerun()