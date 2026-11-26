import streamlit as st
from groq import Groq
from streamlit.errors import StreamlitSecretNotFoundError
st.set_page_config(page_title='AI INTERVIEW ASISSTANT', layout='centered')
st.caption('practice interviews with AI-generated questions and constructive feedback.')
st.caption('Pavitra')
st.write("Department of AI&DS")

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection sucessful")
except(KeyError,FileNotFoundError):
  st.error('GROQ_API_KEY is missing.Add it to streamlit cloud -->App setting')
  st.stop()
  role=st.selection("Select Job Role",[
      "Python Developer",
      "Java Developer",
      "Data Analyst",
      "Machine Learning Engineer",
      "Software Engineer",
      "HR Executive"])              
if st.button("Generate interview questions"):
  
  prompt = "generate 5 interview questions for the role of" + role

  response = client.chat.completions.create(
      model="openai/gpt-oss-120b", messages=[
    {"role":"user","content":prompt}
    ]
)
output = response.choices[0].message.content
st.write(output)
