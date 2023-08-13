import streamlit as st
from audio_recorder_streamlit import audio_recorder
import os

def save_and_return_audio(uploadedfile, session_name):
    # Save the audio file to a given directory with the session name as the title
    file_path = os.path.join("audioDir", session_name + ".wav")
    with open(file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    # Return the name and absolute location of the audio file
    return session_name, os.path.abspath(file_path)

# Create a form with a text input and a submit button
with st.form(key="my_form"):
    session_name = st.text_input(label="Enter session name")
    submit_button = st.form_submit_button(label="Submit")

# If the form is submitted, record and save the audio
if submit_button:
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        # Call the function and display the results
        name, location = save_and_return_audio(audio_bytes, session_name)
        st.write(f"The name of the recorded audio is: **{name}**")
        st.write(f"The absolute location of the recorded audio is: **{location}**")
