import streamlit as st
# from modules.cnf import get_set_of_production
from cyk import is_accepted

title = 'Syntatic Parsing of Indonesia Sentences using CYK Algortihm'

st.set_page_config(layout='wide', page_title=title, menu_items={
    'About': f"""
    ### {title}
    Made with power by Group 5 in Class C  
    Language and Automata Theory Subject  
    """
})

st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)

string_input = st.text_input('Input Sentence', placeholder="ex : saya makan nasi")
list_string = string_input.split(' ')
button_click = st.button('Check', type='primary')

    # action if button clicked
if button_click:
            # show error when no string or just one string entered
    if len(list_string) <= 1:
        st.error("Sentence can't be null or a word.")
            # else, process the filing table
    elif string_input != '':
        st.write('<br><p>Status:</p>', unsafe_allow_html=True)
        is_accepted(string_input)