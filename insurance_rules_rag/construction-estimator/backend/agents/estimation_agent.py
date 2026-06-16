from graph.state import ConstructionState


def estimation_agent(state: ConstructionState):
    print("Estimation Agent Running")

    tasks = state["detected_tasks"]
    costs = state["cost_breakdown"]

    report = f"""
Construction Estimation Report

Walls ({tasks.get('walls', 0)}): ₪{costs.get('walls_cost', 0)}

Kitchen Removal ({tasks.get('kitchen', 0)}): ₪{costs.get('kitchen_cost', 0)}

Water Pipeline ({tasks.get('pipeline', 0)}m): ₪{costs.get('pipeline_cost', 0)}

--------------------------------

Total Project Cost: ₪{costs.get('total_cost', 0)}
"""

    state["final_report"] = report

    return state