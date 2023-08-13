import streamlit as st
import pandas as pd
import tempfile
import os
from time import sleep


from ai_transcriber_model import transcribe_audio, clean_data

# create main columns
_input, result = st.columns([8, 2])
placeholder = st.empty()

placeholder.text(".")

with _input:
    st.subheader("Transcription Dashboard")
    with st.form("my_form"):
    #    mp3 file to transcribe
        uploaded_file = st.file_uploader("Upload File", type=["mp3", "m4a", "wav"])
        submit = st.form_submit_button("Transcribe")


        full_path = None
        if submit:
            if uploaded_file:
                if uploaded_file is not None:
                    # Get the current working directory
                    work_dir = os.getcwd()

                    # Create a folder named uploads if it does not exist
                    upload_dir = os.path.join(work_dir, "uploads")
                    if not os.path.exists(upload_dir):
                        os.makedirs(upload_dir)

                    # Save the uploaded file to the upload folder
                    upload_path = os.path.join(upload_dir, uploaded_file.name)
                    with open(upload_path, "wb") as f:
                        f.write(uploaded_file.read())

                    # Get the full path of the saved file
                    full_path = os.path.abspath(upload_path)

                    # Display the full path

                st.toast('File Uploaded, Trascription in progress, please wait...', icon='😍')
                results = transcribe_audio(full_path)
                
                clean_data(results['text'], uploaded_file.name)

                progress_text = "Cleaning and Building Transcription"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    sleep(0.1)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                # 

                st.markdown(f"""
                ### Transcription for {uploaded_file.name}
                {results['text']}

                    """)    

                # print(results)

with result:
    st.subheader("Services")

    # list of services Include.
    # [Transcription]
    