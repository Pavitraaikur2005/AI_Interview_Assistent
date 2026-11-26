import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI INTERVIEW ASISSTANT', layout='centered')
st.caption('practice interviews with AI-generated questions and constructive feedback.')
st.caption('Pavitra')
st.write("Department of AI&DS")

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY])
  st.write("API connection sucessful")
except(KeyError,FileNotFoundError):
  st.error('GROQ_API_KEY is missing.Add it to streamlit cloud -->App setting')
  st.stop()
