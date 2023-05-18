# utils.py

import streamlit as st
import random
import os

#A list of tasks for each level
levels = {
    1: ['first_word', 'fizzbuzz', 'ft_strcpy', 'ft_strlen', 'ft_swap', 
        'ft_putstr', 'repeat_alpha', 'rev_print', 'rot_13', 'rotone', 
        'search_and_replace', 'ulstr'],
    2: ['alpha_mirror', 'do_op', 'ft_atoi', 'ft_strcmp', 'ft_strcspn', 
        'ft_strdup', 'ft_strpbrk', 'ft_strrev', 'ft_strspn', 'inter', 
        'is_power_of_2', 'last_word', 'max', 'print_bits', 'reverse_bits', 
        'snake_to_camel', 'swap_bits', 'union', 'wdmatch'],
    3: ['add_prime_sum', 'epur_str', 'expand_str', 'ft_atoi_base',
        'ft_list_size', 'ft_range', 'ft_rrange', 'hidenp','lcm',
        'paramsum', 'pgcd', 'print_hex', 'rstr_capitalizer', 
        'str_capitalizer', 'tab_mult'],
    4: ['flood_fill', 'fprime', 'ft_itoa', 'ft_list_foreach', 'ft_list_remove_if',
        'ft_split', 'rev_wstr', 'rostring', 'sort_int_tab', 'sort_list',]
}

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

#Creating a button to start the exam
def start_exam(level, progress_bar):
    if st.button('Start Exam'):
        st.session_state['level'] += 1
        task_name = random.choice(level)
        st.session_state['tasks'].append(task_name)
        progress_bar.progress(min(st.session_state['level'] / 4, 1))

#Creating a button to display the exam
def display_exam():
    for i, task_name in enumerate(st.session_state['tasks'], start=1):
        st.subheader(f'Level {i}')
        expected_files, allowed_functions, description = load_task(task_name)
        st.markdown(f'**Task:** {task_name}\n', unsafe_allow_html=True)
        st.markdown(f'**Expected files:** {expected_files}\n', unsafe_allow_html=True)
        st.markdown(f'**Allowed functions:** {allowed_functions}\n', unsafe_allow_html=True) 
        st.markdown(f'**Description:**\n{description}\n', unsafe_allow_html=True)

#Creating a button to move to the next level
def next_level(level, progress_bar):
    st.write('\n')
    if st.button(f'Next Level (Level {st.session_state["level"] + 1})'):
        st.session_state['level'] += 1
        task_name = random.choice(level)
        st.session_state['tasks'].append(task_name)
        progress_bar.progress(min(st.session_state['level'] / 4, 1))
        st.experimental_rerun()

#Creating a button to start the selected level
def select_level():
    st.sidebar.markdown('<h2 style="text-align: center;">Pick Your Starting Point 🎯</h2>', unsafe_allow_html=True)
    selected_level = st.sidebar.selectbox('Select Level:', list(levels.keys()))
    if st.sidebar.button('Start Selected Level'):
        st.session_state['level'] = selected_level
        st.session_state['tasks'] = [random.choice(levels[i]) for i in range(1, selected_level+1)]
        st.experimental_rerun()

#Creating a button to finish the exam
def finish_exam(progress_bar):
    st.write('\n')
    if st.button('Finish Exam'):
        st.session_state['level'] += 1
        progress_bar.progress(min(st.session_state['level'] / 4, 1))
        st.experimental_rerun()

#Creating a button to start over
def start_over():
    if st.button('Start Over'):
        st.session_state['level'] = 0
        st.session_state['tasks'] = []
        st.experimental_rerun()
