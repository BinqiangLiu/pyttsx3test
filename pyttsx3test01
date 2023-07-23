import streamlit as st
import pyttsx3
import numpy as np
import os

# Function to convert text to speech using pyttsx3
def text_to_speech(text):    
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "english-us")
    # Save the audio in the current directory as "response.mp3"
    engine.save_to_file(text, "response.mp3")
    engine.runAndWait()
    # Read the audio file and return its binary content
    with open("response.mp3", "rb") as file:
        audio_bytes = file.read()
    # Remove the temporary audio file
    os.remove("response.mp3")
    return audio_bytes

# Main function to run the Streamlit app
def main():
    st.title("Audio to Chat App")
    text = "中华人民共和国People's Republic of China"
    # Audio output section
    st.header("Step 2: Listen to the AI Response")
    st.audio(text_to_speech(text), format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
