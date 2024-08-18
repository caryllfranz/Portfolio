import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    responses = [
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
    ]
    
    response = random.choice(responses)
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("CHATBOT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})