from src.agent.state import RequestState
from src.agent.answer_generator.node import AnswerGenerator
from src.agent.message_refiner.node import MessageRefiner

from langgraph.graph import StateGraph, START, END

graph = StateGraph(RequestState)

graph.add_node("answer_generator", AnswerGenerator().answer_generator)
graph.add_node("message_refiner", MessageRefiner().message_refiner)

graph.add_edge(START, "message_refiner")
graph.add_edge("message_refiner", "answer_generator")
graph.add_edge("answer_generator", END)

chat = graph.compile()
