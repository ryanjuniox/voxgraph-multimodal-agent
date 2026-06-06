import streamlit as st

from src.agent.graph import chat


def main():
    st.title("VoxGraph - Multimodal Agent")

    state = {}
    question = st.chat_input(
        "Say or record something",
        accept_audio=True,
    )

    if not question:
        return

    if question and question.text:
        with st.chat_message(name="user"):
            st.write(question.text)
        state["request_type"] = "text"
        state["question"] = question.text
    else:
        with st.chat_message(name="user"):
            st.audio(question.audio)
        state["request_type"] = "audio"
        state["question"] = ""
        state["audio_bytes"] = question.audio.getvalue()

    with st.chat_message(name="ai"):
        response = chat.invoke(state)
        st.write(response["answer"])


main()
