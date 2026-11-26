import streamlit as st
from groq import Groq
from streamlit.errors import StreamlitSecretNotFoundError

st.set_page_config(
    page_title="AI Interview Assistant",
    layout="centered"
)

st.title("AI Interview Assistant")

st.caption(
    "Practice interviews with AI-generated questions and constructive feedback."
)

st.caption("Launched by: ISHWARIYA S ")
st.write("Department of AI & DS")

try:
    api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(api_key=api_key)

    st.success("API connection successful!")

except (KeyError, FileNotFoundError, StreamlitSecretNotFoundError):
    st.error(
        "GROQ_API_KEY is missing. "
        "Add it to your Streamlit secrets."
    )
    st.stop()

role = st.selectbox("Select Job Role",[
                    "Python Developer",
                    "Java Developer",
                    "Data Analyst",
                    "Machine Learning Engineer",
                    "Software Engineer",
                    "HR Executive"
                    ])
if st.button("Generate Interview Questions"):
    prompt="Generate 5 Interview questions for the role of " + role
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
    {"role":"user","content":prompt}
    ]
    )
    output = response.choices[0].message.content
    st.write(output)
