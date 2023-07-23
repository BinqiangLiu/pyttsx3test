import streamlit as st
import pyttsx3
import numpy as np
import os
import ffmpeg
import pyaudio

engine = pyttsx3.init()
engine.setProperty("rate", 150)
#engine.setProperty("voice", "english-us")
text = "The parties recently announced they had settled their disputes and entered into a settlement agreement and patent sublicense deal (see the A123 press release here). Some details of the Patent Sublicense Agreement have been made public. Actually a cross-licensing deal, A123 has taken, or will take, a license to lithium metal phosphate patents developed at UT, a family of electrode metal carbon-coating patents, and several lithium metal phosphate patents licensed to H-Q by Nippon Telephone and Telegraph."
# Save the audio in the current directory as "response.mp3"
engine.save_to_file(text, "response.mp3")
engine.runAndWait()
# Read the audio file and return its binary content
with open("response.mp3", "rb") as file:
    audio_bytes = file.read()
# Remove the temporary audio file
#os.remove("response.mp3")
st.title("Audio to Chat App")
# Audio output section
st.header("Step 2: Listen to the AI Response")
st.audio(audio_bytes, format="audio/mp3", start_time=0)
st.audio(audio_bytes)
