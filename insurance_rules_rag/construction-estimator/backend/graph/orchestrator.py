from langgraph.graph import StateGraph, END

from graph.state import ConstructionState
from agents.input_agent import input_agent
from agents.pdf_agent import pdf_agent
from agents.task_agent import task_agent
from agents.pricing_agent import pricing_agent
from agents.estimation_agent import estimation_agent
def create_graph():

    workflow = StateGraph(ConstructionState)

    workflow.add_node("input_agent", input_agent)
    workflow.add_node("pdf_agent", pdf_agent)

    workflow.set_entry_point("input_agent")
    workflow.add_node("task_agent", task_agent)
    workflow.add_node("pricing_agent", pricing_agent)
    workflow.add_node("estimation_agent", estimation_agent)
    workflow.add_edge("input_agent", "pdf_agent")
    workflow.add_edge("pdf_agent", "task_agent")
    workflow.add_edge("task_agent", "pricing_agent")
    workflow.add_edge("pricing_agent", "estimation_agent")
    workflow.add_edge("estimation_agent", END)

    return workflow.compile()