# import streamlit as st
# import os
# import google.generativeai as genai
# from fontTools.misc.cython import returns
#
# st.header("CHAT PROMPT")
#
# genai.configure(api_key="AIzaSyCbNcbjk9_wbsKwSuwNQflPNi6SquD2CDM")
# model=genai.GenerativeModel("gemini-2.0-flash")
#
#
#
# prompt= st.chat_input("")
# if prompt:
#     if prompt.strip()=="":
#         st.write("Please enter a description")
#     else:
#         with st.spinner("processing..."):
#          try:
#             responce=model.generate_content(prompt)
#             st.write(prompt)
#             st.write(responce.text)
#          except Exception as e:
#              st.write(e)
#
#
#




import streamlit as st
import google.generativeai as genai

# Streamlit page header
st.header("CHAT PROMPT")

# Configure Gemini API
genai.configure(api_key="AIzaSyCbNcbjk9_wbsKwSuwNQflPNi6SquD2CDM")
model = genai.GenerativeModel("gemini-2.0-flash")

# Initialize chat history if not present
if "history" not in st.session_state:
    st.session_state.history = []

# Get user input
prompt = st.chat_input("")

# Process the prompt
if prompt:
    if prompt.strip() == "":
        st.warning("Please enter a description.")
    else:
        with st.spinner("Processing..."):
            try:
                response = model.generate_content(prompt)
                # Store question and answer
                st.session_state.history.append(("You", prompt))
                st.session_state.history.append(("Gemini", response.text))
            except Exception as e:
                st.error(f"Error: {e}")

# Display chat history
for speaker, message in st.session_state.history:
    st.markdown(f"**{speaker}:** {message}")
