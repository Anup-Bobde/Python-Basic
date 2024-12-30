# Gen-AI = text to text generation with frontend (How to run streamlit,see vdo in screen recordings)
# To install generativeai=> pip install -q -U google-generativeai

import streamlit as st
import os

import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown
# from altair.vegalite.v4.api import Chart

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  
os.environ['GEMINI_API_KEY'] = 'AIzaSyCXP_1Q7769CG7cz56ZAbgrQIoxKab389E'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Function to load gemini model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="GEMINI LLM APP")

st.header("Gemini AI BOT Application")

input=st.text_input("Input: ",key="input")

submit=st.button("click me to generate response")

# If ask button is clicked

if submit:
   
    response=get_gemini_response(input)  # get_gemini_response() fun is called & question of input is sent to function as parameter
    st.subheader("The Response is")
    st.write(response)
