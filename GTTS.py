# Converting text to speech using GTTS library and frontend streamlit
import streamlit as st
from gtts import gTTS
import os

# Streamlit app title
st.title("Text-to-Speech Converter created by Sunitha Mekala")

# Input text from the user
text_input = st.text_area("Enter the desired text you want to convert to speech:")

# Button to generate speech
if st.button("Generate Speech"):
    if text_input:
        # Generate speech
        tts = gTTS(text=text_input, slow=False)
        tts.save("output.mp3")
        
        # Play the audio file
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
        
        # Option to download the audio file
        st.download_button(label="Download Audio", data=audio_bytes, file_name="output.mp3", mime="audio/mp3")
    else:
        st.warning("Please enter some text to convert to speech.")

# Footer
st.markdown("Developed using Streamlit and gTTS")