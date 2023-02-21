# Article-Summarizer
Article Summarizer using the <b>OpenAI [ Completion Class model ] API </b> and the <b> Streamlit library </b> to create a simple web application that allows a user to input a scientific article and generate a summary of the article. The user can choose the size of the output summary and save the generated summary to their device.

# Setting Up
1. OpenAI API
```
- To use the OpenAI API, you need to sign up for a free account on the OpenAI website and create a new API key.
- Set the API key as the value of the openai.api_key variable in your code.
- Use the openai library to make requests to the API's endpoints and access its AI-powered text generation capabilities.
```
2. Streamlit secrets
```
- The st.secrets object is a special Streamlit object that allows you to store sensitive information in a secure way, 
  as the secrets are not visible in the source code of your app while testing locally. 
- This is useful for protecting API keys and other sensitive information from being exposed publicly.
- The st.secrets object is accessed like a dictionary, with the keys being the names of the secrets and 
  the values being the secret values themselves.
```
3. Code-Time
```
- Start by importing the required libraries and setting up our OpenAI API key.
- Next, create a text area for the user to enter the text of a scientific article 
  using Streamlit’s text_area function.
- Then add a radio button that allows the user to choose the desired output size, with three options available: 
  “To-The-Point”, “Concise”, and “Detailed”.
```
# Helping Resource
[Summarizing Scientific Articles with OpenAI ✨ and Streamlit 🎈 by Avra ](https://medium.com/@avra42/summarizing-scientific-articles-with-openai-and-streamlit-fdee12aa1a2b)<br>
[ Video- Link ](https://youtu.be/cVBUOQAlrOw)
