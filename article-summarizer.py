# import os
import streamlit as st
# Import the required libraries
import openai


# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]

# Read the text of the article from a file
# with open("article.txt", "r") as f:
#     article_text = f.read()
article_text = st.text_area("Enter your scientific texts to summarize", key="text")
def clear_text():
    st.session_state["text"] = ""
    
st.button("clear text input", on_click=clear_text)
output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text)>100:
    if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Please summarize this scientific article for me in a few sentences: " + article_text,
            max_tokens = out_token,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")
