# streamlit page config
import streamlit as st
from translator_utils import translate

st.set_page_config(
    page_title="Translator",
    page_icon="💡",
    layout="centered"
)

# streamlit page title
st.title("🤖Translator Bot")

col1, col2 = st.columns(2)
with col1:
    input_language_list = ["English", "French", "Japanese", "Korean", "Spanish"]
    input_language = st.selectbox(label="Input Language", options=input_language_list)

with col2:
    output_language_list = [x for x in input_language_list if x != input_language]
    output_language = st.selectbox(label="Output Language", options=output_language_list)

input_text = st.text_area("Help me translate:")

# creating the translate button
if st.button("Translate"):
    translated_text = translate(input_language,output_language,input_text)
    st.success(translated_text)
