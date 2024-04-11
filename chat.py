import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import ollama
import speech_recognition as sr

st.title("💬 Chat with NicK ")
st.markdown("This is an LLM-powered chatbot built using Streamlit and Ollama LLM model.")

# Sidebar contents
with st.sidebar:
    st.title('💬 Chat with NicK 🤗')
    st.markdown('''
    ## About
    Built with:
    - [Streamlit](https://streamlit.io/)
    - [Ollama LLM model](https://ollama.com/library/llama2)
    ''')

    add_vertical_space(2)
    st.write('- **Author:** [Vignesh Swaminathan](https://www.linkedin.com/in/vigneshavmm/)')

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

### Write Message History
for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        st.write("Audio captured")
        
        try:
            text = recognizer.recognize_google(audio)

            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand.")
            return None

## Generator for Streaming Tokens
def generate_response():

    response = ollama.chat(model='vicky', stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]}) 

if st.button("Speak"):
    text = recognize_speech()

    if text:
        st.session_state.messages.append({"role": "user", "content": text})
        st.chat_message("user", avatar="🧑‍💻").write(text)
        st.session_state["full_message"] = ""
        st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
