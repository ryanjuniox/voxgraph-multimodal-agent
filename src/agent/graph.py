from src.agent.state import RequestState
from src.agent.answer_generator.node import AnswerGenerator
from src.agent.transcriber.node import TranscriberAgent
from src.routers.request_type_router import router

from langgraph.graph import StateGraph, START, END

graph = StateGraph(RequestState)

graph.add_node("answer_generator", AnswerGenerator().answer_generator)
graph.add_node("transcriber", TranscriberAgent().transcriber_agent)

graph.add_conditional_edges(
    START,
    router,
    {
        "transcriber": "transcriber",
        "answer_generator": "answer_generator",
    },
)
graph.add_edge("transcriber", "answer_generator")
graph.add_edge("answer_generator", END)

chat = graph.compile()
