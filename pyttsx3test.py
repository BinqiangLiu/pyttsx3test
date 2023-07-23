#使用这个录音模块：https://pypi.org/project/audio-recorder-streamlit/
import streamlit as st
import pyttsx3
import numpy as np
import os
import ffmpeg

# Function to convert text to speech using pyttsx3
def text_to_speech(text):    
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "english-us")    
    engine.save_to_file(text, "response.mp3")     
    engine.runAndWait()
    response_audio = open("response.mp3", "rb")    
    audio_bytes = response_audio.read()
#    with open("response.mp3", "rb") as file:
#        response_audio = file.read()
    #os.remove("response.mp3")
    return audio_bytes

# Main function to run the Streamlit app
def main():
    st.title("Audio to Chat App")
    text = "中华人民共和国People's Republic of China"
        # Audio output section
    st.header("Step 2: Listen to the AI Response")
    st.audio(text_to_speech(text), format="audio/mp3", start_time=0)
#    st.audio(audio_bytes)

if __name__ == "__main__":
    main()
