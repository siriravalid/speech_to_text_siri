import streamlit as st
import speech_recognition as sr
import tempfile
st.title("Voice based speech to text converter-Siri")
st.write("Please record your voice for 10 seconds.")
if st.button("Start Recording"):
    recognizer = sr.Recognizer()
    with st.spinner("Recording..."):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.record(source, duration=10)
                st.write("Recording completed. Processing...")
                text = recognizer.recognize_google(audio_data)
                st.write("Transcribed Text:")
                st.write(text)
                with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                    tmp_file.write(audio_data.get_wav_data())
                    tmp_file.close()
                    st.audio(tmp_file.name, format='audio/wav')
        except sr.UnknownValueError:
            st.write("Sorry, could not understand the audio.")
        except sr.RequestError:
            st.write("Sorry, there was an error with the speech recognition service.")
