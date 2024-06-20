import streamlit as st
from transformers import pipeline
import os
os.environ["api_key"] = "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"

st.write('# Language Translator')

st.button("Button", type="primary")

input1 = st.text_input('Give the input sentence:')

text = 'value' #@param {type:"string"}

translator1 = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
resultHi = translator1(input1, max_length=40)

translator2 = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
resultTe = translator2(input1, max_length=40)

translator3 = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")
resultTa = translator3(input1, max_length=40)

translator4 = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
resultCh = translator4(input1, max_length=40)

if st.button('Hindi'):
    st.write(resultHi)

print(resultHi)

if st.button('French'):
    st.write(resultTe)

print(resultTe)

if st.button('Spanish'):
    st.write(resultTa)

print(resultTa)

if st.button('German'):
    st.write(resultCh)

print(resultCh)
