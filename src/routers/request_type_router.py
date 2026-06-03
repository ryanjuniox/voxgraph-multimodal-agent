def router(state: dict) -> str:
    request_type = state.get("request_type")
    if request_type == "audio":
        return "transcriber"
    return "answer_generator"
