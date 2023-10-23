import string
import streamlit as st

from llm import define

page_title = 'Contextual Dictionary'
st.set_page_config(
        page_title=page_title,
)
st.title(page_title)
st.text('Type in a word and the sentence where it\'s used and get the definition.\nPowered by Claude API.')

sentence = st.text_area('Sentence', 'This is a word in an example sentence.')

stripped_sent = sentence.translate(str.maketrans('', '', string.punctuation))
words = stripped_sent.split(' ')
word = st.selectbox('Word to Define', [''] + list(words), key='word')

st.write('---')
if word:
    st.write(f'The word "{st.session_state.word}" in the sentence means:\n\n{define(word, sentence)}') # type: ignore
