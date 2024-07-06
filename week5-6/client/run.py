import streamlit as st
from engine import explain

add_selectbox = st.sidebar.selectbox(
    "Select an LLM.",
    ("GPT-3.5", "LLaMA 2 7B", "Mistral 7B")
)

st.logo("assets/horizontal.png", icon_image="assets/icon.png")

prompt = st.text_input("Enter a prompt:", "Which country has the highest number of billionaires?")
result = explain(prompt)
# # st.write("The current movie title is", result)
span_template = '<span style="color: #COLOR;">TEXT</span>'
html_content = '<p>\n'
for word in result:
    html_content += span_template.replace("COLOR", word["color"]).replace("TEXT", word["text"])
    html_content += "\n"
html_content += "<p>\n"

st.html(html_content)
