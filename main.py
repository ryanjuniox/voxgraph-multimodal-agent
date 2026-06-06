import streamlit as st

from src.agent.graph import chat
from src.utils.logger import logging


def main():
    st.title("VoxGraph - Multimodal Agent")

    state = {}
    question = st.chat_input(
        "Say or record something",
        accept_audio=True,
    )

    if not question:
        return

    logging.info("Question received from user")

    if question and question.text:
        logging.info("Request type: text | Question: %s", question.text)
        with st.chat_message(name="user"):
            st.write(question.text)
        state["request_type"] = "text"
        state["question"] = question.text
    else:
        logging.info("Request type: audio | Audio bytes received")
        with st.chat_message(name="user"):
            st.audio(question.audio)
        state["request_type"] = "audio"
        state["question"] = ""
        state["audio_bytes"] = question.audio.getvalue()

    logging.info("Invoking agent graph with request_type=%s", state["request_type"])

    with st.chat_message(name="ai"):
        response = chat.invoke(state)
        logging.info("Agent response generated successfully")
        st.write(response["answer"])


main()
