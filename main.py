import streamlit as st

from src.pipelines.audio_pipeline import run as process_audio


def main():
    st.title("VoxGraph - Multimodal Agent")

    audio_value = st.audio_input("Record a voice message")

    if audio_value:
        st.audio(audio_value)

        with st.spinner("Transcrevendo..."):
            text = process_audio(audio_value.getvalue())

        st.subheader("Transcrição")
        st.write(text)


main()
