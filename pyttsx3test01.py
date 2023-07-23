import streamlit as st
import pyttsx3
import io
from pydub import AudioSegment

# Function to convert text to speech using pyttsx3 and pydub
def text_to_speech(text):    
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", "english-us")
    
    # Use pyttsx3 to generate audio
    mp3_data = io.BytesIO()
    engine.save_to_file(text, mp3_data)
    mp3_data.seek(0)
    
    # Convert mp3_data to AudioSegment
    audio = AudioSegment.from_file(mp3_data, format="mp3")
    
    # Convert AudioSegment to bytes
    audio_bytes = audio.export(format="mp3")
    
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
